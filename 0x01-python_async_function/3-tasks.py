#!/usr/bin/env python3
""""a wait random function that returns an asyncio.Task"""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returns asyncio.Task"""

    return asyncio.Task(wait_random(max_delay))
