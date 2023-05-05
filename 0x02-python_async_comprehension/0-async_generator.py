#!/usr/bin/env python3
"""an async generator loops 10 times"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Loops 10 times and waits 1 second
    then yields a random number between 0 and 10"""

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
