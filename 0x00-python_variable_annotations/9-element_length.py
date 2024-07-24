#!/usr/bin/env python3
"""
Function’s parameters & return values
with the appropriate types
"""
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Create a list of tuples where each
    tuple contains a string from the input list & its length.

    Args:
        lst (List[str]): A list of strings.

    Returns:
        List[Tuple[str, int]]: A list of tuples where each
        tuple contains a string & its length.
    """
    return [(i, len(i)) for i in lst]
