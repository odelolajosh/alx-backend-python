#!/usr/bin/env python3
""" safe_first_element """
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ returns the first element if it exists. """
    if lst:
        return lst[0]
    else:
        return None
