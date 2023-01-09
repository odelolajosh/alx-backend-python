#!usr/bin/env python3
""" 2. Measure the runtime """

import time
import asyncio


wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Measures the total execution time for `wait_n` """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - start_time
    return elapsed / n
