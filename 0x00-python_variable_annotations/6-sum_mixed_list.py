#!/usr/bin/env python3
""" sum_mixed_list """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """ returns the sum of a list of float and integers. """
    return sum(mxd_lst)
