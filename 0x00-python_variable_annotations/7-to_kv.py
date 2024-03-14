#!/usr/bin/env python3
'''
Module Doc
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Forms a tuple with the input string and the square of the input int or
    float.

    Parameters:
    - k (str): The input string.
    - v (Union[int, float]): The input integer or float.

    Returns:
    Tuple[str, float]: A tuple with the input string and the square of the
    input int or float.
    """
    return (k, float(v) ** 2)
