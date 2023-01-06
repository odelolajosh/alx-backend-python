#!/usr/bin/env python3
""" element_length """
from collections.abc import Iterable, List, Tuple, Sequence


def elment_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ returns a list of tuple with element and length of element. """
    return [(i, len(i)) for i in lst]
