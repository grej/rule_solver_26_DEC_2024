# scoring.py

import numpy as np
import pandas as pd
from typing import Dict, Union, Optional, Tuple
from dataclasses import dataclass

@dataclass
class ScoreResult:
    """Container for rule scoring results"""
    score: float
    coverage: float
    support: int  # Number of matching samples
    target_improvement: float  # Improvement in target variable
    target_stats: Dict  # Additional statistics about target variable

class RuleScorer:
    """
    Handles scoring of rules based on their effectiveness in driving
    target variables in desired directions.
    """
    def __init__(self, df: pd.DataFrame, target_var: str, direction: str):
        """
        Initialize scorer with dataset and target information.

        Args:
            df: Input DataFrame
            target_var: Name of target variable
            direction: 'maximize'/'minimize' for continuous, category name for categorical
        """
        self.df = df
        self.target_var = target_var
        self.direction = direction
        self.is_categorical = not np.issubdtype(df[target_var].dtype, np.number)

        # Pre-compute target statistics
        if not self.is_categorical:
            self.target_mean = df[target_var].mean()
            self.target_std = df[target_var].std()
            self.target_range = df[target_var].max() - df[target_var].min()

    def get_matching_mask(self, rule: Dict) -> pd.Series:
        """Get boolean mask of samples matching rule conditions."""
        mask = pd.Series(True, index=self.df.index)

        for feature, condition in rule.items():
            if feature == self.target_var:
                continue

            if isinstance(condition, tuple):
                mask &= (self.df[feature] >= condition[0]) & (self.df[feature] <= condition[1])
            else:
                mask &= (self.df[feature] == condition)

        return mask

    def score_continuous(self, rule: Dict) -> ScoreResult:
        """Score rule for continuous target variable."""
        mask = self.get_matching_mask(rule)
        matching_samples = self.df[mask]
        non_matching = self.df[~mask]

        if len(matching_samples) < 3:  # Require minimum samples
            return ScoreResult(
                score=float('-inf'),
                coverage=0,
                support=0,
                target_improvement=0,
                target_stats={}
            )

        # Calculate improvements
        matching_mean = matching_samples[self.target_var].mean()
        matching_std = matching_samples[self.target_var].std()

        if self.direction == 'maximize':
            improvement = (matching_mean - self.target_mean) / self.target_std
        else:
            improvement = (self.target_mean - matching_mean) / self.target_std

        # Calculate coverage with minimum threshold
        coverage = len(matching_samples) / len(self.df)
        min_coverage = max(0.05, 10/len(self.df))  # At least 5% or 10 samples
        coverage_score = coverage if coverage >= min_coverage else coverage * (coverage/min_coverage)

        # Calculate spread penalty
        spread_ratio = matching_std / self.target_std if self.target_std > 0 else 1
        spread_penalty = 1 / (1 + spread_ratio)

        # Combine scores
        final_score = improvement * spread_penalty * np.sqrt(coverage_score)

        return ScoreResult(
            score=final_score,
            coverage=coverage,
            support=len(matching_samples),
            target_improvement=improvement,
            target_stats={
                'matching_mean': matching_mean,
                'matching_std': matching_std,
                'non_matching_mean': non_matching[self.target_var].mean(),
                'improvement_ratio': improvement
            }
        )

    def score_categorical(self, rule: Dict) -> ScoreResult:
        """Score rule for categorical target variable."""
        mask = self.get_matching_mask(rule)
        matching_samples = self.df[mask]
        non_matching = self.df[~mask]

        if len(matching_samples) < 3:
            return ScoreResult(
                score=float('-inf'),
                coverage=0,
                support=0,
                target_improvement=0,
                target_stats={}
            )

        # Calculate class distributions
        matching_dist = matching_samples[self.target_var].value_counts(normalize=True)
        non_matching_dist = non_matching[self.target_var].value_counts(normalize=True)

        # Get target class probability improvement
        target_prob_matching = matching_dist.get(self.direction, 0)
        target_prob_non_matching = non_matching_dist.get(self.direction, 0)
        prob_improvement = target_prob_matching - target_prob_non_matching

        # Calculate coverage score
        coverage = len(matching_samples) / len(self.df)
        min_coverage = max(0.05, 10/len(self.df))
        coverage_score = coverage if coverage >= min_coverage else coverage * (coverage/min_coverage)

        # Calculate purity
        purity = matching_dist.get(self.direction, 0)

        # Combine scores favoring both improvement and purity
        final_score = (prob_improvement * 0.6 + purity * 0.4) * np.sqrt(coverage_score)

        return ScoreResult(
            score=final_score,
            coverage=coverage,
            support=len(matching_samples),
            target_improvement=prob_improvement,
            target_stats={
                'target_prob_matching': target_prob_matching,
                'target_prob_non_matching': target_prob_non_matching,
                'purity': purity,
                'class_distribution': matching_dist.to_dict()
            }
        )

    def score_rule(self, rule: Dict) -> ScoreResult:
        """Score a rule based on target type."""
        if self.is_categorical:
            return self.score_categorical(rule)
        else:
            return self.score_continuous(rule)

def score_improvement(new_score: float,
                     base_score: float,
                     new_coverage: float,
                     base_coverage: float,
                     coverage_weight: float = 0.1) -> float:
    """
    Calculate improvement in score with coverage consideration.

    Args:
        new_score: Score after change
        base_score: Score before change
        new_coverage: Coverage after change
        base_coverage: Coverage before change
        coverage_weight: Weight given to coverage changes

    Returns:
        Combined improvement score
    """
    score_diff = new_score - base_score
    coverage_diff = new_coverage - base_coverage

    return score_diff + coverage_weight * coverage_diff
