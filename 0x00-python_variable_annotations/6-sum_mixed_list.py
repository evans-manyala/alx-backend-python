#!/usr/bin/env python3
"""
Calculates the sum of a list containing
integers and floats
"""
from typing import Union, List


def sum_mixed_list(mixed_list: List[Union[int, float]]) -> float:
    """
    Calculates the sum of a list containing integers and floats.

    Args:
    mixed_list: A list of integers and floats.

    Returns:
    The sum of all elements in the input list.
    """

    return sum(mixed_list)
