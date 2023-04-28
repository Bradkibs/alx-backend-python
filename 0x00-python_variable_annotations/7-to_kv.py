#!/usr/bin/env python3
""" A function that returns a
tuple when given different inputs"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns k and square of v in a tuple"""

    return tuple([k, v * v])
