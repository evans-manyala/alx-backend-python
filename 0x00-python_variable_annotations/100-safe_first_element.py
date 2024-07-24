#!/usr/bin/env python3
"""
Function that safely gets a value
from a dictionary with a default.
"""
from typing import Any, Sequence, Union



def safely_get_value(lst: Sequence[Any]) -> Union[Any, None]):
    """
    Safely get a value from a dictionary with a default.
    """
    if lst:
        return lst[0]
    else:
        return None
