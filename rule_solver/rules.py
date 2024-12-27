# rules.py
import numpy as np
from .utils import infer_feature_types, matches_rule
from .scoring import calculate_rank_score, score_improvement, fast_ranks

def create_rule(point1, point2, continuous_features, categorical_features, df):
    """Create rule with adaptive boundary expansion"""
    rule = {}

    # Handle continuous features with margin
    for feature in continuous_features:
        min_val = min(point1[feature], point2[feature])
        max_val = max(point1[feature], point2[feature])

        # Add substantial margin to create meaningful ranges
        feature_range = max_val - min_val
        if feature_range == 0:  # If points are identical, use dataset range
            all_vals = df[feature].values
            feature_range = np.percentile(all_vals, 90) - np.percentile(all_vals, 10)
        margin = feature_range * 0.5  # 50% margin

        rule[feature] = (min_val - margin, max_val + margin)

    # Handle categorical features
    for feature in categorical_features:
        if point1[feature] == point2[feature]:
            rule[feature] = point1[feature]

    return rule

def generate_rules(df, num_rules=100, target_column='species', min_coverage=0.1):
    """Generate initial rules using smart sampling and density-based expansion"""
    continuous_features, categorical_features = infer_feature_types(df)
    if target_column in continuous_features:
        continuous_features.remove(target_column)

    rules = []

    # Strategy 1: Use percentile-based ranges for each class
    classes = df[target_column].unique()

    for target_class in classes:
        class_df = df[df[target_column] == target_class]

        # Create rules using different percentile ranges
        percentile_pairs = [(20, 80), (10, 90), (30, 70)]

        for lower_pct, upper_pct in percentile_pairs:
            rule = {}

            # Create ranges using percentiles for continuous features
            for feature in continuous_features:
                values = class_df[feature].values
                lower = np.percentile(values, lower_pct)
                upper = np.percentile(values, upper_pct)
                if lower != upper:
                    rule[feature] = (lower, upper)

            # Add any categorical features that strongly correlate with class
            for feature in categorical_features:
                if feature != target_column:
                    mode_val = class_df[feature].mode().iloc[0]
                    mode_ratio = (class_df[feature] == mode_val).mean()
                    if mode_ratio > 0.8:  # Only add if strongly predictive
                        rule[feature] = mode_val

            if rule:  # Only add if we found some defining features
                rules.append(rule)

    # Strategy 2: Density-based point selection
    for _ in range(num_rules // 3):  # Reduced number to make room for percentile rules
        # Sample initial point
        seed_point = df.sample(1).iloc[0]

        # Find nearby points using rank-based distance
        distances = []
        for _, candidate in df.iterrows():
            dist = 0
            for feature in continuous_features:
                # Use rank difference as distance metric
                ranks = fast_ranks(df[feature].values)
                seed_idx = (df[feature] == seed_point[feature]).idxmax()
                candidate_idx = df.index.get_loc(_)
                p1_rank = ranks[seed_idx]
                p2_rank = ranks[candidate_idx]
                dist += (p1_rank - p2_rank) ** 2
            distances.append(np.sqrt(dist))

        # Select point from dense region
        nearest_idx = np.argmin(distances)
        dense_point = df.iloc[nearest_idx]

        rule = create_rule(seed_point, dense_point,
                         continuous_features, categorical_features, df)
        rules.append(rule)

    return rules

def prune_rule(df, rule, target_column='species', min_improvement=0.05, min_features=2):
    """Prune conditions using rank-based scoring"""
    base_metrics = calculate_rank_score(df, rule, target_column)

    if base_metrics is None:
        raise ValueError("Base metrics cannot be None. Ensure calculate_rank_score always returns a valid dictionary.")

    current_rule = rule.copy()
    pruning_history = []

    while True:
        best_improvement = -float('inf')
        best_feature_to_remove = None
        best_new_metrics = None

        for feature in list(current_rule.keys()):
            if feature == target_column:
                continue

            # Ensure we keep minimum number of features
            remaining_features = len([f for f in current_rule if f != target_column])
            if remaining_features < min_features:
                continue

            test_rule = {k: v for k, v in current_rule.items() if k != feature}
            test_metrics = calculate_rank_score(df, test_rule, target_column)

            if test_metrics is None:
                continue

            improvement = score_improvement(
                test_metrics['score'],
                base_metrics['score'],
                test_metrics['coverage'],
                base_metrics['coverage']
            )

            if improvement > best_improvement:
                best_improvement = improvement
                best_feature_to_remove = feature
                best_new_metrics = test_metrics

        if best_improvement < min_improvement or best_feature_to_remove is None:
            break

        current_rule.pop(best_feature_to_remove)
        base_metrics = best_new_metrics

        pruning_history.append({
            'removed_feature': best_feature_to_remove,
            'improvement': best_improvement,
            'metrics': best_new_metrics,
            'current_rule': current_rule.copy()
        })

    return current_rule, base_metrics, pruning_history


def find_best_rules(df, num_rules=5, target_column='species'):
    """Generate, prune and rank rules"""
    rules = generate_rules(df, num_rules, target_column)
    pruned_rules = []

    for rule in rules:
        pruned_rule, metrics, history = prune_rule(df, rule, target_column)
        pruned_rules.append((pruned_rule, metrics, history))

    # Sort by score
    pruned_rules.sort(key=lambda x: x[1]['score'], reverse=True)
    return pruned_rules[:num_rules]  # Return only requested number of rules
