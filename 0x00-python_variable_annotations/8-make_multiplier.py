#!/usr/bin/env python3
"""
Function that multiplies a number by a given multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function that multiplies a number by a given multiplier.

    Args:
    multiplier: The factor to multiply by.

    Returns:
    A function that takes a float & returns its product
    with the multiplier.
  """
    def multiply(number: float) -> float:
        """Multiplies a number by the stored multiplier.

        Args:
        number: The number to multiply.

        Returns:
        The product of the number & the multiplier.
    """
        return number * multiplier
    return make_multiplier
