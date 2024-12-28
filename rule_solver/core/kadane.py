# kadane.py

import numpy as np
from typing import Tuple, Optional
from numba import njit
from dataclasses import dataclass

@dataclass
class KadaneResult:
    """Container for Kadane's algorithm results"""
    start_idx: int
    end_idx: int
    max_sum: float
    values: np.ndarray  # The values in the maximum subarray

@njit
def kadane_basic(arr: np.ndarray) -> Tuple[int, int, float]:
    """
    Basic implementation of Kadane's algorithm for maximum subarray sum.
    Optimized with Numba.

    Args:
        arr: Input array of values

    Returns:
        Tuple of (start_index, end_index, maximum_sum)
    """
    curr_sum = 0.0
    max_sum = float('-inf')
    curr_start = 0
    start = 0
    end = 0

    for i in range(len(arr)):
        if curr_sum <= 0:
            curr_sum = arr[i]
            curr_start = i
        else:
            curr_sum += arr[i]

        if curr_sum > max_sum:
            max_sum = curr_sum
            start = curr_start
            end = i

    return start, end, max_sum

@njit
def kadane_with_minimum_length(arr: np.ndarray, min_length: int) -> Tuple[int, int, float]:
    """
    Kadane's algorithm that enforces a minimum subarray length.

    Args:
        arr: Input array
        min_length: Minimum length of subarray to consider

    Returns:
        Tuple of (start_index, end_index, maximum_sum)
    """
    n = len(arr)
    if n < min_length:
        return 0, n-1, np.sum(arr)

    # First compute sums of all windows of min_length
    curr_sum = np.sum(arr[:min_length])
    max_sum = curr_sum
    best_start = 0
    best_end = min_length - 1

    # Slide the window
    for i in range(min_length, n):
        curr_sum = curr_sum + arr[i] - arr[i - min_length]
        if curr_sum > max_sum:
            max_sum = curr_sum
            best_start = i - min_length + 1
            best_end = i

    # Now try extending the best window
    # Extend left
    curr_sum = max_sum
    i = best_start - 1
    while i >= 0:
        if curr_sum + arr[i] > curr_sum:
            curr_sum += arr[i]
            best_start = i
        i -= 1

    # Extend right
    curr_sum = max_sum
    i = best_end + 1
    while i < n:
        if curr_sum + arr[i] > curr_sum:
            curr_sum += arr[i]
            best_end = i
        i += 1

    return best_start, best_end, max_sum

@njit
def kadane_with_maximum_length(arr: np.ndarray, max_length: int) -> Tuple[int, int, float]:
    """
    Kadane's algorithm that enforces a maximum subarray length.

    Args:
        arr: Input array
        max_length: Maximum length of subarray to consider

    Returns:
        Tuple of (start_index, end_index, maximum_sum)
    """
    n = len(arr)
    max_sum = float('-inf')
    best_start = 0
    best_end = 0

    for length in range(1, min(max_length + 1, n + 1)):
        curr_sum = np.sum(arr[:length])
        if curr_sum > max_sum:
            max_sum = curr_sum
            best_start = 0
            best_end = length - 1

        for i in range(length, n):
            curr_sum = curr_sum + arr[i] - arr[i - length]
            if curr_sum > max_sum:
                max_sum = curr_sum
                best_start = i - length + 1
                best_end = i

    return best_start, best_end, max_sum

def find_optimal_interval(values: np.ndarray,
                         min_length: Optional[int] = None,
                         max_length: Optional[int] = None) -> KadaneResult:
    """
    Find optimal interval in array using appropriate Kadane variant.

    Args:
        values: Input array
        min_length: Minimum length constraint (optional)
        max_length: Maximum length constraint (optional)

    Returns:
        KadaneResult object with optimal interval information
    """
    # Safe standardization
    mean = np.mean(values)
    std = np.std(values)

    if std > 0:
        std_values = (values - mean) / std
    else:
        # If std is 0, all values are the same
        # In this case, we'll just use the centered values
        std_values = values - mean if mean != 0 else values

    # Choose appropriate Kadane variant
    if min_length is not None:
        start, end, max_sum = kadane_with_minimum_length(std_values, min_length)
    elif max_length is not None:
        start, end, max_sum = kadane_with_maximum_length(std_values, max_length)
    else:
        start, end, max_sum = kadane_basic(std_values)

    return KadaneResult(
        start_idx=start,
        end_idx=end,
        max_sum=max_sum,
        values=values[start:end+1]
    )

def find_optimal_split(values: np.ndarray) -> Tuple[int, float]:
    """
    Find optimal split point in array that maximizes difference between sides.

    Args:
        values: Input array

    Returns:
        Tuple of (split_index, score)
    """
    cumsum = np.cumsum(values)
    total = cumsum[-1]
    n = len(values)

    best_score = float('-inf')
    best_split = 0

    for i in range(1, n-1):
        left_mean = cumsum[i] / (i+1)
        right_mean = (total - cumsum[i]) / (n-i-1)
        score = abs(left_mean - right_mean)

        if score > best_score:
            best_score = score
            best_split = i

    return best_split, best_score
