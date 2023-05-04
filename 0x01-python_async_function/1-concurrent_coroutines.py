#!/usr/bin/env python3
"""Multiple coroutines at the same time"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """returns a list of the delays sorted in ascending order"""

    await_queue: List[float] = [wait_random(max_delay) for _ in range(n)]
    result = await asyncio.gather(*await_queue)
    return sorted(result)
