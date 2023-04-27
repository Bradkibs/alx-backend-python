#!/usr/bin/env python3
"""Sum of mixed list"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """returns the sum as float"""

    sum: float = 0
    for item in mxd_lst:
        sum += item
    return sum
