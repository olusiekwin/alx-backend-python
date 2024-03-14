#!/usr/bin/env python3
'''
Module Docs
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculates the sum of a list of floats.

    Parameters:
    - input_list (List[float]): The list of floats.

    Returns:
    float: The sum of the input list.
    """
    return float(sum(input_list))
