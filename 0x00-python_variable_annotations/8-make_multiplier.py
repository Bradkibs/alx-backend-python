#!/usr/bin/env python3
"""A function that takes a multiplier and returns a function
that multiplies a float by multiplier"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float
    by multiplier"""
    def inner_function(number: float) -> float:
        """The inner function that multiplies the two nums"""
        return multiplier * number
    return inner_function
