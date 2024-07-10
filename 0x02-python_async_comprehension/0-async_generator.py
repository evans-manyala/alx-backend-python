#!/usr/bin/env python3
"""A Python module to loop 10 times."""

import random
import asyncio


async def async_generator():
    """
    An asynchronous generator that yields a random number between 0 and 10,
    every second, for a total of 10 times.
    """
    for _ in range(10):
        await asyncio.sleep(1)  # asynchronously wait for 1 second
        yield random.uniform(0, 10)  # yield a random number between 0 and 10
