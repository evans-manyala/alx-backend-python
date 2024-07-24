#!/usr/bin/env python3
"""
Function that safely gets a value
from a dictionary with a default.
"""
from typing import TypeVar, Dict, Any, Optional

T = TypeVar('T')

def safely_get_value(dct: Dict[Any, T], key: Any, default: Optional[T] = None) -> Optional[T]:
    """
    Safely get a value from a dictionary with a default.

    Args:
        dct (Dict[Any, T]): The dictionary to get the value from.
        key (Any): The key to look for in the dictionary.
        default (Optional[T]): The default value to return
        if the key is not found. Default is None.

    Returns:
        Optional[T]: The value from the dictionary
        if the key is found, otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
