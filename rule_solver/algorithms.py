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
