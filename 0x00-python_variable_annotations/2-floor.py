#!/usr/bin/env python3
"""An type annotated implementation of floor"""


def floor(n: float) -> int:
    """Implementation of floor function"""

    return int(n - (n % 1))
