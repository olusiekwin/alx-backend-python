#!/usr/bin/env python3
'''
Module Doc
'''
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples,
    where each tuple contains an element from the input list and its length.

    Parameters:
    - lst (Iterable[Sequence]): The input iterable of sequences.

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples containing elements
    from the input list
                               and their corresponding lengths.
    """
    return [(i, len(i)) for i in lst]
