#!/usr/bin/env python3
"""Contains a method that starts wait_r n times
with a specified delay between each call.
"""

import asyncio
from typing import List

wait_r = __import__('0-basic_async_syntax').wait_r


async def wait_r(n: int, max_delay: int) -> List[float]:
    """Start wait_r n times with a specified delay between each call.
    
    Args:
        n: number of times to start wait_r
        max_delay: max delay between each call
    Returns:
        list of delays in the order they were completed
    """
    tasks = [asyncio.create_task(wait_r(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
