#!/usr/bin/env python3
"""
Function’s parameters and return values
annotated with the appropriate types.
"""
from typing import List, Tuple, Sequence


def element_length(lst: List[Sequence[str]]) -> List[Tuple[str, int]]:
    """
    Create a list of tuples where each tuple contains
    a string from the input list and its length.

    Args:
        lst (List[Sequence[str]]): A list of sequences where
        each sequence is expected to be a string.

    Returns:
        List[Tuple[str, int]]: A list of tuples where
        each tuple contains a string and its length.
    """
    return [(i, len(i)) for i in lst]
