#!/usr/bin/env python3
"""
Function that safely gets a value
from a dictionary with a default.
"""
from typing import Any,Union, Sequence



def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely get a value from a dictionary with a default.
    """
    if lst:
        return lst[0]
    else:
        return None
