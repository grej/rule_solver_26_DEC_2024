# reducer.py

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from ..core.scoring import RuleScorer, ScoreResult

@dataclass
class ReductionResult:
    """Container for dimensionality reduction results"""
    initial_rule: Dict
    final_rule: Dict
    removed_features: List[str]
    initial_score: float
    final_score: float
    reduction_steps: List[Dict]

class RuleReducer:
    """
    Handles dimensionality reduction of rules by removing features
    that don't significantly contribute to rule performance.
    """
    def __init__(self, df: pd.DataFrame,
                 target_var: str,
                 direction: str,
                 min_features: int = 1,
                 min_improvement: float = 0.001):
        """
        Initialize rule reducer.

        Args:
            df: Input DataFrame
            target_var: Name of target variable
            direction: 'maximize'/'minimize' for continuous, category for categorical
            min_features: Minimum number of features to keep
            min_improvement: Minimum improvement needed to remove feature
        """
        self.df = df
        self.target_var = target_var
        self.direction = direction
        self.min_features = min_features
        self.min_improvement = min_improvement
        self.scorer = RuleScorer(df, target_var, direction)

    def _try_remove_feature(self,
                           rule: Dict,
                           feature: str) -> Tuple[float, Optional[Dict]]:
        """
        Try removing a feature and evaluate the result.

        Args:
            rule: Current rule dictionary
            feature: Feature to try removing

        Returns:
            Tuple of (score, new_rule) or (score, None) if removal not beneficial
        """
        test_rule = rule.copy()
        del test_rule[feature]

        if len(test_rule) < self.min_features:
            return float('-inf'), None

        score = self.scorer.score_rule(test_rule).score
        return score, test_rule

    def reduce_rule(self, rule: Dict) -> ReductionResult:
        """
        Reduce rule dimensionality by removing non-contributing features.

        Args:
            rule: Initial rule dictionary

        Returns:
            ReductionResult containing reduced rule and reduction history
        """
        current_rule = rule.copy()
        removed_features = []
        reduction_steps = []

        # Get initial score
        initial_score = self.scorer.score_rule(current_rule).score
        current_score = initial_score

        improved = True
        while improved and len(current_rule) > self.min_features:
            improved = False
            best_improvement = -float('inf')
            best_feature = None
            best_new_rule = None

            # Try removing each feature
            for feature in list(current_rule.keys()):
                new_score, new_rule = self._try_remove_feature(current_rule, feature)
                improvement = new_score - current_score

                if improvement > best_improvement and improvement > self.min_improvement:
                    best_improvement = improvement
                    best_feature = feature
                    best_new_rule = new_rule

            if best_feature is not None:
                step = {
                    'removed_feature': best_feature,
                    'old_score': current_score,
                    'new_score': current_score + best_improvement,
                    'improvement': best_improvement,
                    'remaining_features': list(best_new_rule.keys())
                }
                reduction_steps.append(step)

                current_rule = best_new_rule
                current_score += best_improvement
                removed_features.append(best_feature)
                improved = True

        return ReductionResult(
            initial_rule=rule,
            final_rule=current_rule,
            removed_features=removed_features,
            initial_score=initial_score,
            final_score=current_score,
            reduction_steps=reduction_steps
        )

    def reduce_by_correlation(self,
                            rule: Dict,
                            corr_threshold: float = 0.8) -> ReductionResult:
        """
        Reduce rule dimensionality by removing highly correlated features.

        Args:
            rule: Initial rule dictionary
            corr_threshold: Correlation threshold for feature removal

        Returns:
            ReductionResult with correlation-based reduction results
        """
        continuous_features = [f for f, v in rule.items() if isinstance(v, tuple)]
        if len(continuous_features) < 2:
            return ReductionResult(
                initial_rule=rule,
                final_rule=rule,
                removed_features=[],
                initial_score=self.scorer.score_rule(rule).score,
                final_score=self.scorer.score_rule(rule).score,
                reduction_steps=[]
            )

        # Calculate correlation matrix
        corr_matrix = self.df[continuous_features].corr().abs()

        # Find highly correlated pairs
        current_rule = rule.copy()
        removed_features = []
        reduction_steps = []
        initial_score = self.scorer.score_rule(rule).score
        current_score = initial_score

        for i in range(len(continuous_features)):
            for j in range(i + 1, len(continuous_features)):
                if corr_matrix.iloc[i, j] > corr_threshold:
                    feat1, feat2 = continuous_features[i], continuous_features[j]

                    # Try removing each feature and keep the better one
                    score1, rule1 = self._try_remove_feature(current_rule, feat1)
                    score2, rule2 = self._try_remove_feature(current_rule, feat2)

                    if score1 > score2 and score1 > current_score:
                        step = {
                            'removed_feature': feat1,
                            'correlation_with': feat2,
                            'correlation_value': corr_matrix.iloc[i, j],
                            'old_score': current_score,
                            'new_score': score1
                        }
                        reduction_steps.append(step)
                        current_rule = rule1
                        current_score = score1
                        removed_features.append(feat1)
                    elif score2 > current_score:
                        step = {
                            'removed_feature': feat2,
                            'correlation_with': feat1,
                            'correlation_value': corr_matrix.iloc[i, j],
                            'old_score': current_score,
                            'new_score': score2
                        }
                        reduction_steps.append(step)
                        current_rule = rule2
                        current_score = score2
                        removed_features.append(feat2)

        return ReductionResult(
            initial_rule=rule,
            final_rule=current_rule,
            removed_features=removed_features,
            initial_score=initial_score,
            final_score=current_score,
            reduction_steps=reduction_steps
        )
