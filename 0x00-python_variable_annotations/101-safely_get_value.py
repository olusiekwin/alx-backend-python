#!/usr/bin/env python3
'''
Module Doc
'''
from typing import TypeVar, Mapping, Any, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieves the value associated with the given key from the
    dictionary.

    Parameters:
    - dct (Mapping): The input dictionary.
    - key (Any): The key to retrieve the value for.
    - default (Union[T, None], optional): The default value to return if the
    key is not present. Defaults to None.

    Returns:
    Union[Any, T]: The value associated with the key, or the default value
    if the key is not present.
    """
    if key in dct:
        return dct[key]
    else:
        return default
