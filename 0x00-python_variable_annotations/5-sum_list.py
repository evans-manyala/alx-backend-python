#!/usr/bin/env python3
"""Function calculates sum of a list of floats"""
from typing import List


def sum_list(input_list: list[float]) -> float:
    """Calculates the sum of a list of floats.

    Args:
    input_list: A list of float numbers.

    Returns:
    The sum of all elements in the input list.
    """

    return sum(input_list)
