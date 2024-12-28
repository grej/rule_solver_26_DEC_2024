# stabilizer.py

import numpy as np
import pandas as pd
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from ..core.kadane import find_optimal_interval, KadaneResult
from ..core.scoring import RuleScorer, ScoreResult

@dataclass
class StabilizationResult:
    """Container for stabilization results"""
    rule: Dict
    score: float
    improvements: List[Dict]  # Track changes made during stabilization
    final_metrics: ScoreResult

class RuleStabilizer:
    """
    Handles stabilization of rules by optimizing intervals and conditions.
    Uses Kadane's algorithm to find optimal intervals while maintaining
    other conditions.
    """
    def __init__(self, df: pd.DataFrame,
                 target_var: str,
                 direction: str,
                 min_samples: int = 10):
        """
        Initialize rule stabilizer.

        Args:
            df: Input DataFrame
            target_var: Name of target variable
            direction: 'maximize'/'minimize' for continuous, category for categorical
            min_samples: Minimum samples required in rule
        """
        self.df = df
        self.target_var = target_var
        self.direction = direction
        self.min_samples = min_samples
        self.scorer = RuleScorer(df, target_var, direction)

# stabilizer.py - just the _optimize_feature_interval method

    def _optimize_feature_interval(self,
                                rule: Dict,
                                feature: str,
                                current_score: float) -> Tuple[Optional[Tuple[float, float]], float]:
        """
        Optimize interval for a single feature using Kadane's algorithm.

        Args:
            rule: Current rule dictionary
            feature: Feature to optimize
            current_score: Current rule score

        Returns:
            Tuple of (new_bounds, new_score) or (None, current_score) if no improvement
        """
        # Get data matching all other conditions
        mask = pd.Series(True, index=self.df.index)
        for feat, condition in rule.items():
            if feat == feature:  # Skip current feature
                continue
            if isinstance(condition, tuple):
                mask &= (self.df[feat] >= condition[0]) & (self.df[feat] <= condition[1])
            else:
                mask &= (self.df[feat] == condition)

        filtered_df = self.df[mask].copy()
        if len(filtered_df) < self.min_samples:
            return None, current_score

        # Prepare values for Kadane's algorithm
        if isinstance(self.direction, str) and self.direction in ['maximize', 'minimize']:
            # For continuous targets
            values = filtered_df[self.target_var].values
            if self.direction == 'minimize':
                values = -values
        else:
            # For categorical targets
            values = np.where(filtered_df[self.target_var] == self.direction, 1, -1)

        # Find optimal interval
        sorted_indices = np.argsort(filtered_df[feature].values)
        sorted_values = values[sorted_indices]
        result = find_optimal_interval(sorted_values)

        if result.max_sum <= 0:
            return None, current_score

        # Get new bounds from optimal interval
        sorted_feature_values = filtered_df[feature].values[sorted_indices]
        new_bounds = (
            sorted_feature_values[result.start_idx],
            sorted_feature_values[result.end_idx]
        )

        # Test new bounds
        test_rule = rule.copy()
        test_rule[feature] = new_bounds
        new_score = self.scorer.score_rule(test_rule).score

        if new_score > current_score:
            return new_bounds, new_score
        return None, current_score

    def stabilize_rule(self,
                      rule: Dict,
                      max_iterations: int = 5,
                      min_improvement: float = 0.001) -> StabilizationResult:
        """
        Stabilize a rule by iteratively optimizing its intervals.

        Args:
            rule: Rule dictionary to stabilize
            max_iterations: Maximum optimization iterations
            min_improvement: Minimum improvement required to continue

        Returns:
            StabilizationResult containing stabilized rule and improvement history
        """
        current_rule = rule.copy()
        improvements = []
        current_score = self.scorer.score_rule(current_rule).score

        for iteration in range(max_iterations):
            made_improvement = False

            # Try optimizing each continuous feature
            for feature, condition in list(current_rule.items()):
                if not isinstance(condition, tuple):  # Skip categorical features
                    continue

                new_bounds, new_score = self._optimize_feature_interval(
                    current_rule, feature, current_score)

                if new_bounds is not None:
                    improvement = {
                        'iteration': iteration,
                        'feature': feature,
                        'old_bounds': condition,
                        'new_bounds': new_bounds,
                        'score_improvement': new_score - current_score
                    }
                    improvements.append(improvement)

                    current_rule[feature] = new_bounds
                    current_score = new_score
                    made_improvement = True

            if not made_improvement:
                break

        # Get final metrics
        final_metrics = self.scorer.score_rule(current_rule)

        return StabilizationResult(
            rule=current_rule,
            score=current_score,
            improvements=improvements,
            final_metrics=final_metrics
        )

    def stabilize_categorical(self, rule: Dict) -> Tuple[Dict, float]:
        """
        Stabilize categorical features by testing removal/addition.

        Args:
            rule: Current rule dictionary

        Returns:
            Tuple of (stabilized_rule, score)
        """
        current_rule = rule.copy()
        current_score = self.scorer.score_rule(current_rule).score

        # Try removing each categorical condition
        for feature, value in list(current_rule.items()):
            if isinstance(value, tuple):  # Skip continuous features
                continue

            # Test removing this categorical condition
            test_rule = current_rule.copy()
            del test_rule[feature]

            test_score = self.scorer.score_rule(test_rule).score
            if test_score > current_score:
                current_rule = test_rule
                current_score = test_score

        return current_rule, current_score
