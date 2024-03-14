#!/usr/bin/env python3
'''
Module Doc
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Parameters:
    - multiplier (float): The multiplier to be used in the returned function.

    Returns:
    Callable[[float], float]: A function that takes a float and multiplies
    it by the given multiplier.
    """
    func: Callable[[float], float] = lambda value: value * multiplier
    return func
