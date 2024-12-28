# rules.py
import numpy as np
import pandas as pd
from typing import Dict, Union, List, Tuple
from .utils import infer_feature_types
from .optimization import RuleOptimizer


def fast_ranks(x):
    """Simple ranking function using numpy only"""
    temp = x.argsort()
    ranks = np.empty_like(temp)
    ranks[temp] = np.arange(len(x))
    return (ranks + 1) / (len(x) + 1)  # Add 1 to avoid 0s

def calculate_directional_score(df, rule, target_var, direction) -> Dict[str, Union[float, int, str, None]]:
    """
    Calculate score based on how well the rule drives a target variable in desired direction.
    """
    def matches_rule(row, rule):
        if target_var in rule:  # Remove target from rule conditions
            return False
        for feature, value in rule.items():
            if isinstance(value, tuple):
                min_val, max_val = value
                if not (min_val <= row[feature] <= max_val):
                    return False
            else:
                if row[feature] != value:
                    return False
        return True

    # Get matching samples
    matching_mask = df.apply(lambda row: matches_rule(row, rule), axis=1)

    if matching_mask.sum() == 0:
        return {
            'score': 0.0,
            'direction_score': 0.0,
            'coverage': 0.0,
            'matching_samples': 0,
        }

    matching_df = df[matching_mask]
    non_matching_df = df[~matching_mask]

    # Calculate directional score based on variable type
    if direction in ['maximize', 'minimize']:
        # For continuous variables
        matching_vals = matching_df[target_var].values
        non_matching_vals = non_matching_df[target_var].values

        # Get medians for comparison
        matching_median = np.median(matching_vals)
        non_matching_median = np.median(non_matching_vals)

        # Calculate how well the rule separates values in desired direction
        if direction == 'maximize':
            direction_score = (matching_median - non_matching_median) / non_matching_median
        else:  # minimize
            direction_score = (non_matching_median - matching_median) / non_matching_median

        # Calculate spread within matching samples
        matching_iqr = np.percentile(matching_vals, 75) - np.percentile(matching_vals, 25)
        total_iqr = np.percentile(df[target_var], 75) - np.percentile(df[target_var], 25)
        spread_score = 1 - (matching_iqr / total_iqr if total_iqr > 0 else 1)

    else:
        # For categorical variables (direction is desired category)
        matching_counts = matching_df[target_var].value_counts(normalize=True)
        non_matching_counts = non_matching_df[target_var].value_counts(normalize=True)

        # Calculate how much more prevalent the desired category is in matching samples
        matching_rate = matching_counts.get(direction, 0)
        non_matching_rate = non_matching_counts.get(direction, 0)

        direction_score = matching_rate - non_matching_rate
        spread_score = matching_rate  # For categorical, spread is just purity

    # Calculate coverage with penalty for very small rules
    min_samples = max(10, len(df) * 0.05)  # At least 10 samples or 5% of data
    coverage = matching_mask.sum() / len(df)
    coverage_score = coverage if matching_mask.sum() >= min_samples else coverage * 0.5

    # Combine scores
    final_score = (direction_score * 0.6 + spread_score * 0.4) * np.sqrt(coverage_score)

    return {
        'score': final_score,
        'direction_score': direction_score,
        'spread_score': spread_score,
        'coverage': coverage,
        'matching_samples': matching_mask.sum(),
        'target_stats': {
            'matching_median': np.median(matching_df[target_var]) if direction in ['maximize', 'minimize'] else None,
            'non_matching_median': np.median(non_matching_df[target_var]) if direction in ['maximize', 'minimize'] else None,
            'matching_rate': matching_rate if direction not in ['maximize', 'minimize'] else None,
            'non_matching_rate': non_matching_rate if direction not in ['maximize', 'minimize'] else None
        }
    }

def score_improvement(new_score, base_score, new_coverage, base_coverage,
                     coverage_weight=0.1):
    """Calculate improvement in score with coverage penalty/bonus"""
    return (new_score - base_score) + coverage_weight * (new_coverage - base_coverage)

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

def generate_rules(df, num_rules=100, target_var=None):
    """Generate initial rules using percentile ranges and density-based sampling"""
    continuous_features, categorical_features = infer_feature_types(df)
    if target_var in continuous_features:
        continuous_features.remove(target_var)
    if target_var in categorical_features:
        categorical_features.remove(target_var)

    rules = []

    # Strategy 1: Generate rules using percentile ranges for features
    percentile_pairs = [(20, 80), (10, 90), (30, 70)]

    for lower_pct, upper_pct in percentile_pairs:
        # Create multiple rules with different feature combinations
        feature_combinations = [(1,), (2,)]  # Try rules with 1 or 2 features

        for n_features in feature_combinations:
            # Randomly select n features
            selected_features = np.random.choice(
                continuous_features,
                size=min(len(n_features), len(continuous_features)),
                replace=False
            )

            rule = {}
            for feature in selected_features:
                values = df[feature].values
                lower = np.percentile(values, lower_pct)
                upper = np.percentile(values, upper_pct)
                if lower != upper:
                    rule[feature] = (lower, upper)

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

def prune_rule(df, rule, target_var, direction, min_improvement=0.05, min_features=2):
    """Prune conditions using directional scoring"""
    base_metrics = calculate_directional_score(df, rule, target_var, direction)

    if base_metrics is None:
        raise ValueError("Base metrics cannot be None. Ensure scoring always returns a valid dictionary.")

    current_rule = rule.copy()
    pruning_history = []

    while True:
        best_improvement = -float('inf')
        best_feature_to_remove = None
        best_new_metrics = None

        for feature in list(current_rule.keys()):
            if feature == target_var:
                continue

            # Ensure we keep minimum number of features
            remaining_features = len([f for f in current_rule if f != target_var])
            if remaining_features < min_features:
                continue

            test_rule = {k: v for k, v in current_rule.items() if k != feature}
            test_metrics = calculate_directional_score(df, test_rule, target_var, direction)

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

def find_best_rules(df, num_rules=5, target_var=None, direction=None, search_multiplier=4):
    """
    Generate, prune, optimize and rank rules for driving target_var in specified direction.

    Args:
        df: DataFrame with data
        num_rules: Number of rules to return
        target_var: Variable to optimize
        direction: 'maximize'/'minimize' for continuous, or category for categorical
        search_multiplier: Multiple of num_rules to search initially
    """
    if target_var is None:
        raise ValueError("Must specify target_var")
    if direction is None:
        raise ValueError("Must specify direction (maximize/minimize or category)")

    # Remove target variable from rule generation
    features_to_use = [col for col in df.columns if col != target_var]

    # Generate more initial rules for better coverage
    initial_rules = generate_rules(
        df[features_to_use],
        num_rules * search_multiplier,
        target_var
    )

    # Prune rules
    pruned_rules = []
    for rule in initial_rules:
        pruned_rule, metrics, history = prune_rule(df, rule, target_var, direction)
        pruned_rules.append((pruned_rule, metrics, history))

    # Create optimizer and optimize rules
    optimizer = RuleOptimizer(df, target_var, direction)
    optimized_rules = []

    for rule, metrics, history in pruned_rules:
        # Optimization returns (rule, history)
        optimized_rule, opt_history = optimizer.optimize_rule(rule)

        # Calculate new metrics for optimized rule
        if isinstance(optimized_rule, tuple):  # If optimized_rule is a tuple, extract the rule part
            optimized_rule = optimized_rule[0]

        new_metrics = calculate_directional_score(df, optimized_rule, target_var, direction)

        # Combine histories
        combined_history = history + opt_history

        optimized_rules.append((optimized_rule, new_metrics, combined_history))

    # Sort by score and slice
    optimized_rules.sort(key=lambda x: x[1]['score'], reverse=True)

    return optimized_rules[:num_rules]


# rules.py

def matches_rule(row, rule, target_var=None):
    """Check if a row matches rule conditions."""
    for feature, value in rule.items():
        if feature == target_var:
            continue

        # Only try numeric comparison for tuple conditions
        if isinstance(value, tuple):
            try:
                min_val, max_val = value
                if not (pd.to_numeric(min_val) <= pd.to_numeric(row[feature]) <= pd.to_numeric(max_val)):
                    return False
            except (TypeError, ValueError):
                # If conversion fails, do direct comparison
                if row[feature] != value:
                    return False
        else:
            if row[feature] != value:
                return False
    return True
