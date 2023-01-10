#!/usr/bin/env python3
""" 0. Async Generator """
from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """ Yield a random number after async waiting for 1s 10 times. """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
