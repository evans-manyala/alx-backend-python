#!/usr/bin/env python3
"""
Function that safely gets a value
from a dictionary with a default.
"""
from typing import TypeVar, Dict, Any, Mapping, Union

T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: T = None) -> \
        Union[Any, T]:
    """
    Safely get a value from a dictionary with a default.

    Args:
         dct -> dictionary
        key -> dict key
        default -> None
    Return: default
    """
    if key in dct:
        return dct[key]
    else:
        return default
