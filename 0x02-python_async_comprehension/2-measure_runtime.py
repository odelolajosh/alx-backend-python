#!/usr/bin/env python3
""" 2.  Run time for 4 parallel comprehensions """
import asyncio
from typing import List
import time


async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """ Measure total runtime of executing 4 `async_comprehension`
    in parallel.
    """
    start_time = time.perf_counter()
    await asyncio.gather(*([async_comprehension()] * 4))
    return time.perf_counter() - start_time
