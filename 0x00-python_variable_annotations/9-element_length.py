#!/usr/bin/env python3
"""Annotating a duck typed iterable object"""


from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returning the appropriate types"""
    return [(i, len(i)) for i in lst]
