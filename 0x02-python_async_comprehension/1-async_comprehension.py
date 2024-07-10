#!/usr/bin/env python3
"""A Python module to loop 10 times
and collect numbers using
comprehensions."""

import random
import asyncio
from typing import List


async def async_generator():
    """
    An asynchronous generator that yields a
    random number between 0 and 10,
    every second, for a total of 10 times.
    """
    for _ in range(10):
        await asyncio.sleep(1)  # asynchronously wait for 1 second
        yield random.uniform(0, 10)  # yield a random number between 0 and 10


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers from async_generator
    using an async comprehension.
    """
    return [number async for number in async_generator()]
