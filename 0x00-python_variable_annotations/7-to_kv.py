#!/usr/bin/env python3
"""
Function creates a tuple from a string & the square of a number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Converts a key and a value to a key-value tuple.
    
    Args:
    k: The key as a string.
    v: The value as an integer or float.
    
    Returns:
    A tuple containing the key and the square of the value.
    """
    return k, float(v) ** 2
