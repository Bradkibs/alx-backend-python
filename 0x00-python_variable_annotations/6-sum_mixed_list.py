#!/usr/bin/env python3
"""Sum of mixed list"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns the sum as float"""
    return float(sum(mxd_lst))
