#!/usr/bin/env python3
"""A type annotated sum"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """returns the sum as float"""

    sum: float = 0
    for item in input_list:
        sum += item
    return sum
