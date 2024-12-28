### DIRECTORY ./rule_solver FOLDER STRUCTURE ###
rule_solver/
    algorithms.py
    scoring.py
    optimization.py
    rules.py
    utils.py
    indexed_dataset.py
### DIRECTORY ./rule_solver FOLDER STRUCTURE ###

### DIRECTORY ./rule_solver FLATTENED CONTENT ###
### ./rule_solver/algorithms.py BEGIN ###
# algorithms.py
"""
Core implementation of algorithms for rule discovery and optimization.
"""
import numpy as np
from numba import njit
import pandas as pd
from typing import Tuple, List, Dict, Optional

@njit
def kadane_numba(outcomes: np.ndarray) -> float:
    """
    Implements Kadane's algorithm to find the maximum sum subarray.

    Parameters:
        outcomes: 1D array of standardized outcome values

    Returns:
        float: max_sum representing the maximum separation
    """
    max_sum = -np.inf
    current_sum = 0.0
    for i in range(len(outcomes)):
        if current_sum <= 0:
            current_sum = outcomes[i]
        else:
            current_sum += outcomes[i]
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum

def find_interval(df: pd.DataFrame,
                 feature_column: str,
                 outcome_column: str,
                 max_sum: float) -> Tuple[float, float]:
    """
    Finds the optimal interval [A, B] where the sum is maximized.

    Parameters:
        df: Input dataset
        feature_column: The feature column to analyze
        outcome_column: The outcome column name
        max_sum: Maximum separation value from Kadane's algorithm

    Returns:
        Tuple of (A, B) representing interval bounds
    """
    sorted_df = df.sort_values(by=feature_column).reset_index(drop=True)
    current_sum = 0.0
    start = 0
    best_start = 0
    best_end = 0

    for i in range(len(sorted_df)):
        if current_sum <= 0:
            start = i
            current_sum = sorted_df.at[i, outcome_column]
        else:
            current_sum += sorted_df.at[i, outcome_column]

        if current_sum >= max_sum / 2:
            best_start = start
            best_end = i
            break

    return sorted_df.at[best_start, feature_column], sorted_df.at[best_end, feature_column]

def optimize_intervals(df: pd.DataFrame,
                      feature_columns: List[str],
                      outcome_column: str,
                      current_intervals: Optional[Dict[str, Tuple[float, float]]] = None) -> Dict[str, Tuple[float, float]]:
    """
    Optimizes intervals for all features using Kadane's algorithm.

    Parameters:
        df: Input dataset
        feature_columns: List of feature columns to optimize
        outcome_column: Name of the outcome column
        current_intervals: Optional dict of current intervals to optimize from

    Returns:
        Dict mapping feature names to optimal (min, max) intervals
    """
    optimized_intervals = {}

    # Standardize outcome for Kadane's algorithm
    outcomes = df[outcome_column].values
    outcomes = (outcomes - np.mean(outcomes)) / np.std(outcomes)

    for feature in feature_columns:
        # If we have current intervals, use them to filter data
        working_df = df.copy()
        if current_intervals:
            for f, (min_val, max_val) in current_intervals.items():
                if f != feature:  # Don't filter on the feature we're optimizing
                    working_df = working_df[
                        (working_df[f] >= min_val) &
                        (working_df[f] <= max_val)
                    ]

        # Run Kadane's algorithm
        feature_outcomes = outcomes[working_df.index]
        max_sum = kadane_numba(feature_outcomes)

        # Find optimal interval
        min_val, max_val = find_interval(working_df, feature, outcome_column, max_sum)
        optimized_intervals[feature] = (min_val, max_val)

    return optimized_intervals

### ./rule_solver/algorithms.py END ###

### ./rule_solver/scoring.py BEGIN ###
import numpy as np
from typing import Dict, Union, Tuple, Literal

def fast_ranks(x):
    """Simple ranking function using numpy only"""
    temp = x.argsort()
    ranks = np.empty_like(temp)
    ranks[temp] = np.arange(len(x))
    return (ranks + 1) / (len(x) + 1)  # Add 1 to avoid 0s

def calculate_rank_score(df, rule, target_column='species'):
    """
    Enhanced scoring function that balances separation quality with class recall
    while considering within-class spread.
    """
    def matches_rule(row, rule):
        for feature, value in rule.items():
            if feature == target_column:
                continue
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
            'separation_score': 0.0,
            'recall_score': 0.0,
            'coverage': 0.0,
            'matching_samples': 0,
            'dominant_class': None
        }

    matching_df = df[matching_mask]
    non_matching_df = df[~matching_mask]

    # Get class distribution and dominant class
    class_counts = matching_df[target_column].value_counts()
    dominant_class = class_counts.index[0]

    # Calculate class recall for dominant class
    total_in_class = len(df[df[target_column] == dominant_class])
    matching_in_class = len(matching_df[matching_df[target_column] == dominant_class])
    class_recall = matching_in_class / total_in_class if total_in_class > 0 else 0

    # Calculate feature scores for continuous features
    continuous_features = [f for f, v in rule.items()
                         if isinstance(v, tuple) and f != target_column]
    feature_scores = {}

    for feature in continuous_features:
        values = df[feature].values
        normalized_ranks = fast_ranks(values)

        matching_ranks = normalized_ranks[matching_mask]
        nonmatching_ranks = normalized_ranks[~matching_mask]

        # Median separation between classes
        rank_separation = abs(np.percentile(matching_ranks, 50) -
                            np.percentile(nonmatching_ranks, 50))

        # Within-class spread for target class
        target_mask = matching_df[target_column] == dominant_class
        if target_mask.any():
            target_ranks = matching_ranks[target_mask]
            rank_spread = np.percentile(target_ranks, 75) - np.percentile(target_ranks, 25)
            # Penalize high spread within target class
            spread_penalty = 1 / (1 + rank_spread)
        else:
            spread_penalty = 0

        feature_scores[feature] = rank_separation * spread_penalty

    # Calculate separation score
    separation_score = np.mean(list(feature_scores.values())) if feature_scores else 0

    # Calculate purity (proportion of dominant class in matches)
    purity = class_counts.iloc[0] / len(matching_df)

    # Calculate coverage (relative to total dataset)
    coverage = len(matching_df) / len(df)

    # For categorical features, boost score if they help with classification
    categorical_features = [f for f, v in rule.items()
                          if not isinstance(v, tuple) and f != target_column]
    if categorical_features:
        categorical_boost = sum(1 for f in categorical_features
                              if rule[f] == dominant_class) / len(categorical_features)
    else:
        categorical_boost = 0

    # Combine scores with emphasis on meaningful coverage
    # Calculate minimum required coverage based on dataset size
    min_coverage = max(0.1, 10 / len(df))  # At least 10 samples or 10% of data

    # Apply coverage penalty if below minimum
    coverage_score = coverage if coverage >= min_coverage else coverage * (coverage / min_coverage)

    # Combine scores favoring rules with good separation AND good coverage
    base_score = (
        separation_score * 0.4 +  # Continuous feature separation
        class_recall * 0.3 +      # Recall of dominant class
        purity * 0.3             # Class purity in matches
    )

    # Use sigmoid-like function to favor higher coverage when base_score is good
    coverage_weight = 1 / (1 + np.exp(-10 * (base_score - 0.5)))  # Sigmoid centered at 0.5
    final_score = base_score * (1 + coverage_weight * coverage)

    return {
        'score': final_score,
        'separation_score': separation_score,
        'recall_score': class_recall,
        'purity': purity,
        'coverage': coverage,
        'matching_samples': len(matching_df),
        'dominant_class': dominant_class,
        'feature_scores': feature_scores
    }

def calculate_directional_score(df, rule, target_var, direction: Union[Literal['maximize'],
                                                                     Literal['minimize'], str]) \
                                                                     -> Dict[str, Union[float, int, str, None]]:
    """
    Calculate score based on how well the rule drives a target variable in desired direction.

    Args:
        df: DataFrame with all data
        rule: Dictionary of feature conditions
        target_var: Variable to optimize
        direction: Either 'maximize'/'minimize' for continuous variables,
                  or specific category for categorical variables
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

### ./rule_solver/scoring.py END ###

### ./rule_solver/optimization.py BEGIN ###
# optimization.py
"""
Rule optimization and stabilization using iterative improvement.
"""
from typing import Dict, List, Tuple, Optional
import numpy as np
import pandas as pd
from .scoring import calculate_directional_score

class RuleOptimizer:
    def __init__(self, df: pd.DataFrame, target_var: str, direction: str):
        """
        Initialize rule optimizer.
        """
        self.df = df
        self.target_var = target_var
        self.direction = direction

        # Compute dataset statistics once
        self.feature_ranges = {}
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        for col in numeric_cols:
            self.feature_ranges[col] = {
                'min': df[col].min(),
                'max': df[col].max(),
                'median': df[col].median(),
                'q1': df[col].quantile(0.25),
                'q3': df[col].quantile(0.75)
            }

    def validate_rule(self, rule: Dict) -> bool:
        """Check if a rule matches any data points."""
        if not rule:
            return False

        try:
            matching_mask = self.df.apply(
                lambda row: self._matches_rule(row, rule), axis=1)
            matches = matching_mask.sum() >= max(3, len(self.df) * 0.01)  # At least 3 samples or 1%
            return matches
        except:
            return False

    def optimize_rule(self, rule: Dict,
                     min_improvement: float = 0.0001,  # Much lower threshold
                     max_iterations: int = 20) -> Tuple[Dict, List]:
        """
        Optimize a rule through iterative boundary adjustments.
        """
        print(f"\nStarting optimization with rule: {rule}")
        optimization_history = []

        # Start with base rule and score
        current_rule = rule.copy()
        if not self.validate_rule(current_rule):
            print("Initial rule validation failed")
            return current_rule, optimization_history

        try:
            base_metrics = calculate_directional_score(self.df, current_rule,
                                                     self.target_var, self.direction)
            base_score = base_metrics.get('score', 0)
            print(f"Initial score: {base_score:.4f}")
        except Exception as e:
            print(f"Error calculating base score: {e}")
            return current_rule, optimization_history

        for iteration in range(max_iterations):
            print(f"\nIteration {iteration + 1}:")
            made_improvement = False
            best_improvement = 0
            best_rule = None
            best_history_entry = None

            # Try more aggressive variations
            for feature, condition in list(current_rule.items()):
                if not isinstance(condition, tuple):
                    continue

                try:
                    min_val = float(condition[0])
                    max_val = float(condition[1])
                    feature_range = max_val - min_val

                    # Get feature statistics
                    if feature in self.feature_ranges:
                        feat_stats = self.feature_ranges[feature]

                        # More aggressive variations
                        variations = [
                            # Large expansions
                            (min_val - feature_range*0.5, max_val + feature_range*0.5),
                            (min_val - feature_range*0.3, max_val + feature_range*0.3),

                            # Large contractions
                            (min_val + feature_range*0.3, max_val - feature_range*0.3),
                            (min_val + feature_range*0.2, max_val - feature_range*0.2),

                            # Shifts
                            (min_val - feature_range*0.5, max_val - feature_range*0.5),
                            (min_val + feature_range*0.5, max_val + feature_range*0.5),

                            # Data-driven bounds
                            (feat_stats['q1'], feat_stats['q3']),
                            (feat_stats['min'], feat_stats['q3']),
                            (feat_stats['q1'], feat_stats['max']),

                            # Original boundaries with small adjustments
                            (min_val * 0.9, max_val * 1.1),
                            (min_val * 1.1, max_val * 0.9)
                        ]

                        print(f"\nTrying variations for {feature}")
                        for idx, new_bounds in enumerate(variations):
                            test_rule = current_rule.copy()
                            test_rule[feature] = new_bounds

                            if not self.validate_rule(test_rule):
                                continue

                            try:
                                new_metrics = calculate_directional_score(
                                    self.df, test_rule, self.target_var, self.direction)
                                improvement = new_metrics.get('score', 0) - base_score

                                if improvement > 0:
                                    print(f"  Variation {idx}: improvement = {improvement:.6f}")

                                if improvement > best_improvement:
                                    best_improvement = improvement
                                    best_rule = test_rule.copy()
                                    best_history_entry = {
                                        'step': 'optimization',
                                        'feature': str(feature),
                                        'change': 'interval_adjustment',
                                        'initial_score': base_score,
                                        'final_score': base_score + improvement,
                                        'improvement': improvement,
                                        'old_bounds': condition,
                                        'new_bounds': new_bounds
                                    }
                            except Exception as e:
                                print(f"Error testing variation: {e}")
                                continue

                except Exception as e:
                    print(f"Error processing feature {feature}: {e}")
                    continue

            # Apply best improvement found in this iteration
            if best_improvement > min_improvement and best_rule is not None:
                current_rule = best_rule
                base_score += best_improvement
                optimization_history.append(best_history_entry)
                made_improvement = True
                print(f"\nMade improvement: {best_improvement:.6f}")
                print(f"New rule: {current_rule}")
            else:
                print("No improvement found in this iteration")

            if not made_improvement:
                break

        print(f"\nOptimization complete. Final score: {base_score:.4f}")
        return current_rule, optimization_history

    def optimize_rules(self, rules: List[Dict]) -> List[Tuple[Dict, List]]:
        """Optimize a list of rules."""
        return [self.optimize_rule(rule) for rule in rules]

### ./rule_solver/optimization.py END ###

### ./rule_solver/rules.py BEGIN ###
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

### ./rule_solver/rules.py END ###

### ./rule_solver/utils.py BEGIN ###
# utils.py
import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype

def infer_feature_types(df):
    """Split features into continuous and categorical"""
    continuous_features = []
    categorical_features = []
    for col in df.columns:
        if is_numeric_dtype(df[col]):
            continuous_features.append(col)
        else:
            categorical_features.append(col)
    return continuous_features, categorical_features

def matches_rule(row, rule, target_var):
    """Check if a row matches rule conditions"""
    for feature, value in rule.items():
        if feature == target_var:
            continue
        if isinstance(value, tuple):
            min_val, max_val = value
            if not (min_val <= row[feature] <= max_val):
                return False
        else:
            if row[feature] != value:
                return False
    return True

def create_unicode_histogram(values, bins=10, width=30):
    """Create a simple unicode histogram."""
    hist, bin_edges = np.histogram(values, bins=bins)
    max_count = max(hist)

    # Unicode block characters from least to most filled
    blocks = ' ▁▂▃▄▅▆▇█'

    lines = []
    for count, edge in zip(hist, bin_edges[:-1]):
        bar_len = int((count / max_count) * width)
        bar = blocks[-1] * bar_len
        lines.append(f"{edge:6.2f} | {bar:<{width}} | {count:3d}")

    return '\n'.join(lines)

def visualize_rule_impact(df, rule, target_var, direction):
    """Create text visualization of rule's impact on target variable distribution."""
    matching_mask = df.apply(lambda row: matches_rule(row, rule, target_var), axis=1)
    matching_df = df[matching_mask]
    non_matching_df = df[~matching_mask]
    total_matching = len(matching_df)

    lines = [
        "Rule Impact Analysis",
        "=" * 50,
        f"\nMatching Samples: {total_matching} ({total_matching/len(df):.1%} of data)"
    ]

    # Show target variable distribution
    if direction in ['maximize', 'minimize']:
        matching_median = np.median(matching_df[target_var])
        non_matching_median = np.median(non_matching_df[target_var])

        lines.append(f"\n{target_var} Distribution:")
        lines.append(f"Matching samples median: {matching_median:.2f}")
        lines.append("\nMatching samples:")
        hist = create_unicode_histogram(matching_df[target_var].values)
        lines.append(hist)

        lines.append(f"\nNon-matching samples median: {non_matching_median:.2f}")
        lines.append("Non-matching samples:")
        hist = create_unicode_histogram(non_matching_df[target_var].values)
        lines.append(hist)

        improvement = ((matching_median - non_matching_median) / non_matching_median * 100
                      if direction == 'maximize' else
                      (non_matching_median - matching_median) / non_matching_median * 100)
        lines.append(f"\nImprovement: {improvement:+.1f}%")

    else:
        # For categorical target
        matching_counts = matching_df[target_var].value_counts(normalize=True)
        non_matching_counts = non_matching_df[target_var].value_counts(normalize=True)

        lines.append(f"\n{target_var} Distribution:")
        lines.append("\nMatching samples:")
        for cat, pct in matching_counts.items():
            lines.append(f"{cat:12} | {'█' * int(pct * 20):<20} | {pct:.1%}")

        lines.append("\nNon-matching samples:")
        for cat, pct in non_matching_counts.items():
            lines.append(f"{cat:12} | {'█' * int(pct * 20):<20} | {pct:.1%}")

        target_improvement = (matching_counts.get(direction, 0) -
                            non_matching_counts.get(direction, 0)) * 100
        lines.append(f"\nTarget class improvement: {target_improvement:+.1f}%")

    # Show distribution for all continuous features
    continuous_features = [f for f, v in rule.items() if isinstance(v, tuple)]
    if continuous_features:
        lines.append("\nFeature Distributions (Matching Samples):")
        for feature in continuous_features:
            lines.append(f"\n{feature}:")
            hist = create_unicode_histogram(matching_df[feature].values)
            lines.append(hist)
            if feature in rule:
                min_val, max_val = rule[feature]
                lines.append(f"Rule range: [{min_val:.2f}, {max_val:.2f}]")

    return '\n'.join(lines)

# utils.py (update the format_rule_for_human function)

# utils.py
def format_rule_for_human(rule, metrics, history):
    """Format a rule and its metrics into a readable string."""
    lines = []
    lines.append("=" * 50)

    # Format conditions
    lines.append("Rule Conditions:")
    rule_dict = rule if isinstance(rule, dict) else dict(rule)
    for feature, value in rule_dict.items():
        if isinstance(value, tuple):
            try:
                # Convert numpy values to float for cleaner printing
                min_val = round(float(value[0]), 3)
                max_val = round(float(value[1]), 3)
                lines.append(f"  {feature}: {min_val} to {max_val}")
            except:
                lines.append(f"  {feature}: {value[0]} to {value[1]}")
        else:
            lines.append(f"  {feature}: {value}")

    # Format key metrics
    lines.append("\nPerformance:")
    lines.append(f"  Score: {metrics['score']:.3f}")
    lines.append(f"  Direction Score: {metrics['direction_score']:.3f}")
    lines.append(f"  Coverage: {metrics['coverage']:.3f} ({metrics['matching_samples']} samples)")

    # Add target variable statistics if available
    if 'target_stats' in metrics:
        lines.append("\nTarget Variable Statistics:")
        stats = metrics['target_stats']
        if stats['matching_median'] is not None:
            lines.append(f"  Matching Median: {stats['matching_median']:.3f}")
            lines.append(f"  Non-matching Median: {stats['non_matching_median']:.3f}")
        if stats['matching_rate'] is not None:
            lines.append(f"  Matching Rate: {stats['matching_rate']:.3f}")
            lines.append(f"  Non-matching Rate: {stats['non_matching_rate']:.3f}")

    # Format history - handle both pruning and optimization steps
    if history:
        lines.append("\nRule Evolution:")
        for step in history:
            if 'removed_feature' in step:
                lines.append(f"  Pruned: {step['removed_feature']} "
                          f"(improvement: {step['improvement']:.3f})")
            elif 'step' in step and step['step'] == 'optimization':
                if 'change' in step:
                    lines.append(f"  Optimization: {step['change']} on {step['feature']} "
                              f"improved score from {step['initial_score']:.3f} "
                              f"to {step['final_score']:.3f} "
                              f"(gain: {step['improvement']:.3f})")
                else:
                    lines.append(f"  Optimization: score improved from {step['initial_score']:.3f} "
                              f"to {step['final_score']:.3f} "
                              f"(gain: {step['improvement']:.3f})")

    return '\n'.join(lines) + '\n'

def save_rules_to_file(rules, df, filename='rules_output.txt', target_var=None, direction=None):
    """Save rules to a text file with visualizations."""
    with open(filename, 'w') as f:
        f.write(f"Generated Rules Report\n")
        f.write(f"Target: {target_var} ({direction})\n")
        f.write(f"Date: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        for i, (rule, metrics, history) in enumerate(rules, 1):
            f.write(f"Rule {i}\n")
            f.write(format_rule_for_human(rule, metrics, history))
            f.write("\nDistribution Analysis:\n")
            f.write(visualize_rule_impact(df, rule, target_var, direction))
            f.write("\n\n")

### ./rule_solver/utils.py END ###

### ./rule_solver/indexed_dataset.py BEGIN ###
# indexed_dataset.py
"""
Memory-efficient indexed dataset implementation for fast rule discovery.
"""
import numpy as np
from typing import Tuple, List, Dict
import pandas as pd

class IndexedDataset:
    def __init__(self, data: np.ndarray, outcome_column_index: int):
        """
        Preprocesses and indexes the dataset for efficient queries.

        Parameters:
            data: The dataset to index
            outcome_column_index: The column index used for the outcome
        """
        self.n_features = data.shape[1]
        self.outcome_column_index = outcome_column_index
        self.indices = []
        self.sorted_features = []
        self.cumulative_sums = []
        self.outcome = data[:, outcome_column_index]

        # Preprocess each column
        for i in range(self.n_features):
            if i == outcome_column_index:
                continue

            # Sort the feature and compute cumulative sums
            sorted_indices = np.argsort(data[:, i])
            sorted_feature = data[sorted_indices, i]
            sorted_outcome = self.outcome[sorted_indices]
            cumulative_sum = np.cumsum(sorted_outcome)

            self.indices.append(sorted_indices)
            self.sorted_features.append(sorted_feature)
            self.cumulative_sums.append(cumulative_sum)

    def query(self, feature_index: int) -> Tuple[float, float, float, np.ndarray]:
        """
        Finds the best rule for a given feature index using precomputed indices and sums.

        Parameters:
            feature_index: The index of the feature to query

        Returns:
            tuple: (A, B, max_separation, indices_in_rule)
        """
        sorted_feature = self.sorted_features[feature_index]
        cumulative_sum = self.cumulative_sums[feature_index]
        total_sum = cumulative_sum[-1]

        best_start = 0
        best_end = 0
        max_separation = float('-inf')
        start = 0

        for end in range(len(sorted_feature)):
            inside_sum = cumulative_sum[end] - (cumulative_sum[start - 1] if start > 0 else 0)
            outside_sum = total_sum - inside_sum

            # Calculate separation (difference between inside and outside sums)
            separation = inside_sum - outside_sum

            if separation > max_separation:
                max_separation = separation
                best_start = start
                best_end = end

            # If current interval becomes negative, start new interval
            if separation < 0:
                start = end + 1

        A = sorted_feature[best_start]
        B = sorted_feature[best_end]
        indices_in_rule = self.indices[feature_index][best_start:best_end + 1]

        return A, B, max_separation, indices_in_rule

    def query_with_conditions(self, feature_index: int,
                            conditions: Dict[int, Tuple[float, float]]) -> Tuple[float, float, float, np.ndarray]:
        """
        Queries a feature while respecting existing conditions on other features.

        Parameters:
            feature_index: Index of feature to query
            conditions: Dictionary mapping feature indices to (min, max) bounds

        Returns:
            tuple: (A, B, max_separation, indices_in_rule)
        """
        # Create mask for all conditions
        mask = np.ones(len(self.outcome), dtype=bool)
        for feat_idx, (min_val, max_val) in conditions.items():
            if feat_idx != feature_index:
                feat_data = self.sorted_features[feat_idx]
                feat_indices = self.indices[feat_idx]
                condition_mask = (feat_data >= min_val) & (feat_data <= max_val)
                mask[feat_indices[~condition_mask]] = False

        # Apply mask to feature data and recalculate
        sorted_indices = self.indices[feature_index][mask[self.indices[feature_index]]]
        sorted_feature = self.sorted_features[feature_index][mask[self.indices[feature_index]]]
        sorted_outcome = self.outcome[sorted_indices]
        cumulative_sum = np.cumsum(sorted_outcome)

        # Find best interval on filtered data
        total_sum = cumulative_sum[-1] if len(cumulative_sum) > 0 else 0
        best_start = 0
        best_end = 0
        max_separation = float('-inf')
        start = 0

        for end in range(len(sorted_feature)):
            inside_sum = cumulative_sum[end] - (cumulative_sum[start - 1] if start > 0 else 0)
            outside_sum = total_sum - inside_sum
            separation = inside_sum - outside_sum

            if separation > max_separation:
                max_separation = separation
                best_start = start
                best_end = end

            if separation < 0:
                start = end + 1

        A = sorted_feature[best_start] if len(sorted_feature) > 0 else None
        B = sorted_feature[best_end] if len(sorted_feature) > 0 else None
        indices_in_rule = sorted_indices[best_start:best_end + 1] if len(sorted_indices) > 0 else np.array([])

        return A, B, max_separation, indices_in_rule

### ./rule_solver/indexed_dataset.py END ###

### DIRECTORY ./rule_solver FLATTENED CONTENT ###
