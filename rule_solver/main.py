# main.py

import pandas as pd
import numpy as np
from typing import List, Dict, Optional
from dataclasses import dataclass
import logging
from datetime import datetime

from .core.sampling import PairSampler
from .core.hyperrect import HyperRectangle
from .core.kadane import find_optimal_interval
from .core.scoring import RuleScorer, ScoreResult

from .optimization.stabilizer import RuleStabilizer, StabilizationResult
from .optimization.reducer import RuleReducer, ReductionResult

from .utils.validation import (validate_dataframe, validate_target,
                             validate_rule, validate_hyperrect_bounds)
from .utils.feature_utils import FeatureAnalyzer

@dataclass
class RuleDiscoveryResult:
    """Container for complete rule discovery results"""
    rules: List[Dict]
    scores: List[float]
    metrics: List[ScoreResult]
    reduction_history: List[ReductionResult]
    stabilization_history: List[StabilizationResult]
    feature_importance: Dict[str, float]
    runtime_seconds: float

class RuleDiscoverer:
    """
    Main class for rule discovery pipeline.
    Coordinates sampling, rule creation, optimization, and evaluation.
    """
    def __init__(self,
                 df: pd.DataFrame,
                 target_var: str,
                 direction: str,
                 min_samples: int = 10,
                 random_seed: int = 42):
        """
        Initialize rule discoverer.

        Args:
            df: Input DataFrame
            target_var: Target variable name
            direction: 'maximize'/'minimize' for continuous, category for categorical
            min_samples: Minimum samples required in rule
            random_seed: Random seed for reproducibility
        """
        # Validate inputs
        validate_dataframe(df)
        validate_target(df, target_var, direction)

        self.df = df
        self.target_var = target_var
        self.direction = direction
        self.min_samples = min_samples

        # Initialize components
        self.feature_analyzer = FeatureAnalyzer(df)
        self.pair_sampler = PairSampler(df, seed=random_seed)
        self.scorer = RuleScorer(df, target_var, direction)
        self.stabilizer = RuleStabilizer(df, target_var, direction, min_samples)
        self.reducer = RuleReducer(df, target_var, direction)

        # Setup logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def discover_rules(self,
                      num_rules: int = 5,
                      num_pairs: Optional[int] = None,
                      max_iterations: int = 5) -> RuleDiscoveryResult:
        """
        Execute complete rule discovery pipeline.

        Args:
            num_rules: Number of rules to return
            num_pairs: Number of pairs to sample (defaults to num_rules * 20)
            max_iterations: Maximum optimization iterations

        Returns:
            RuleDiscoveryResult containing discovered rules and history
        """
        start_time = datetime.now()

        if num_pairs is None:
            num_pairs = num_rules * 20

        self.logger.info(f"Starting rule discovery with {num_pairs} pairs...")

        # 1. Sample pairs
        pairs = self.pair_sampler.sample_pairs(num_pairs)
        self.logger.info(f"Sampled {len(pairs)} pairs")

        # 2. Create initial rules
        continuous_features = self.feature_analyzer.get_continuous_features()
        categorical_features = self.feature_analyzer.get_categorical_features()

        hyperrect = HyperRectangle(continuous_features, categorical_features)
        initial_rules = []

        for point1, point2 in pairs:
            rule = hyperrect.create_from_points(point1, point2)
            if rule and validate_rule(rule, self.df, self.min_samples)[0]:
                initial_rules.append(rule)

        self.logger.info(f"Created {len(initial_rules)} valid initial rules")

        # 3. Process each rule
        final_rules = []
        reduction_history = []
        stabilization_history = []

        for rule in initial_rules:
            # First reduce dimensionality
            reduction_result = self.reducer.reduce_rule(rule)
            reduction_history.append(reduction_result)
            reduced_rule = reduction_result.final_rule

            # Then stabilize the rule
            stabilization_result = self.stabilizer.stabilize_rule(
                reduced_rule, max_iterations=max_iterations)
            stabilization_history.append(stabilization_result)

            final_rules.append(stabilization_result.rule)

        # 4. Score and rank rules
        rule_scores = []
        rule_metrics = []

        for rule in final_rules:
            metrics = self.scorer.score_rule(rule)
            rule_scores.append(metrics.score)
            rule_metrics.append(metrics)

        # Sort by score
        sorted_indices = np.argsort(rule_scores)[::-1]
        top_rules = [final_rules[i] for i in sorted_indices[:num_rules]]
        top_scores = [rule_scores[i] for i in sorted_indices[:num_rules]]
        top_metrics = [rule_metrics[i] for i in sorted_indices[:num_rules]]

        # Calculate feature importance
        features = continuous_features + categorical_features
        feature_importance = self.feature_analyzer.calculate_feature_importance(
            self.target_var, features)


        runtime = (datetime.now() - start_time).total_seconds()

        self.logger.info(f"Rule discovery completed in {runtime:.2f} seconds")

        return RuleDiscoveryResult(
            rules=top_rules,
            scores=top_scores,
            metrics=top_metrics,
            reduction_history=reduction_history,
            stabilization_history=stabilization_history,
            feature_importance=feature_importance,
            runtime_seconds=runtime
        )

def format_rule(rule: Dict) -> str:
    """Format rule as readable string."""
    parts = []
    for feature, condition in rule.items():
        if isinstance(condition, tuple):
            parts.append(f"{feature}: [{condition[0]:.3f}, {condition[1]:.3f}]")
        else:
            parts.append(f"{feature}: {condition}")
    return " AND ".join(parts)

def main():
    """Example usage of rule discovery pipeline."""
    # Load data
    df = pd.read_csv("example_data.csv")

    # Initialize discoverer
    discoverer = RuleDiscoverer(
        df=df,
        target_var="target",
        direction="maximize"
    )

    # Discover rules
    result = discoverer.discover_rules(
        num_rules=5,
        num_pairs=100,
        max_iterations=5
    )

    # Print results
    print("\nDiscovered Rules:")
    print("=" * 50)

    for i, (rule, score) in enumerate(zip(result.rules, result.scores), 1):
        print(f"\nRule {i}:")
        print(f"Score: {score:.4f}")
        print(f"Conditions: {format_rule(rule)}")
        print("-" * 30)

    print(f"\nTotal runtime: {result.runtime_seconds:.2f} seconds")

if __name__ == "__main__":
    main()
