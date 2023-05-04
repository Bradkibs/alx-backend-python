#!/usr/bin/env python3
"""An asynchronous coroutine that takes in an integer
with default value of 10 and waits a random number
between the set integer and 0"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """returns a random waited delay time"""
    answer = random.uniform(0, max_delay)
    await asyncio.sleep(answer)
    return answer
