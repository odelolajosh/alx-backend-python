#!/usr/bin/env python3
""" to_kv """
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ returns the parameters in a tuple. """
    return (k, v**2)
