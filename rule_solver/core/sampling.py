# sampling.py

import numpy as np
import pandas as pd
from typing import List, Optional, Tuple, Set
import random
from itertools import combinations

# default max attempts
MAXATTEMPTS = 10

class PairSampler:
    """
    Handles sampling of data point pairs for rule generation.
    Maintains unique pairs and ensures reproducibility.
    """
    def __init__(self, df: pd.DataFrame, seed: int = 42):
        """
        Initialize the pair sampler.

        Args:
            df: Input DataFrame
            seed: Random seed for reproducibility
        """
        self.df = df
        self.used_pairs: Set[Tuple[int, int]] = set()
        random.seed(seed)
        np.random.seed(seed)

    def sample_pairs(self, n_pairs: int) -> List[Tuple[pd.Series, pd.Series]]:
        """
        Sample unique pairs of points from the dataset.

        Args:
            n_pairs: Number of pairs to sample

        Returns:
            List of tuples, each containing two data points as pd.Series
        """
        pairs = []
        max_attempts = n_pairs * MAXATTEMPTS  # Avoid infinite loops
        attempts = 0

        while len(pairs) < n_pairs and attempts < max_attempts:
            # Sample two different indices
            idx1, idx2 = np.random.choice(len(self.df), size=2, replace=False)
            pair_key = tuple(sorted([idx1, idx2]))  # Sort to ensure (1,2) and (2,1) are same

            # Check if this pair is new
            if pair_key not in self.used_pairs:
                self.used_pairs.add(pair_key)
                pairs.append((self.df.iloc[idx1], self.df.iloc[idx2]))

            attempts += 1

        if len(pairs) < n_pairs:
            print(f"Warning: Could only generate {len(pairs)} unique pairs")

        return pairs

def sample_all_pairs(df: pd.DataFrame, max_pairs: Optional[int] = None) -> List[Tuple[pd.Series, pd.Series]]:
    """
    Generate all possible pairs up to max_pairs.

    Args:
        df: Input DataFrame
        max_pairs: Maximum number of pairs to generate (None for all possible pairs)

    Returns:
        List of tuples, each containing two data points as pd.Series
    """
    all_indices = range(len(df))
    all_pairs = list(combinations(all_indices, 2))

    if max_pairs and max_pairs < len(all_pairs):
        selected_pairs = random.sample(all_pairs, max_pairs)
    else:
        selected_pairs = all_pairs

    return [(df.iloc[i], df.iloc[j]) for i, j in selected_pairs]

def stratified_pair_sampling(df: pd.DataFrame,
                           target_column: str,
                           n_pairs: int,
                           seed: int = 42) -> List[Tuple[pd.Series, pd.Series]]:
    """
    Sample pairs with stratification based on target variable.
    Ensures representation across different target values.

    Args:
        df: Input DataFrame
        target_column: Name of target variable column
        n_pairs: Number of pairs to sample
        seed: Random seed

    Returns:
        List of tuples, each containing two data points
    """
    random.seed(seed)
    np.random.seed(seed)

    # Group by target value
    groups = df.groupby(target_column)
    pairs = []

    # Calculate pairs per group
    n_groups = len(groups)
    base_pairs_per_group = n_pairs // n_groups
    extra_pairs = n_pairs % n_groups

    for i, (_, group) in enumerate(groups):
        # Add extra pair to some groups if needed
        group_pairs = base_pairs_per_group + (1 if i < extra_pairs else 0)

        if len(group) >= 2:  # Need at least 2 points to make a pair
            indices = group.index.tolist()
            for _ in range(group_pairs):
                if len(indices) >= 2:
                    idx1, idx2 = random.sample(indices, 2)
                    pairs.append((df.loc[idx1], df.loc[idx2]))

    return pairs
