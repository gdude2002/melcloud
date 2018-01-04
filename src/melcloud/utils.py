# coding=utf-8
import arrow
from datetime import datetime

from inflection import underscore as to_underscore
__author__ = "Gareth Coles"


def fix_list_keys(l: list, convert_function=to_underscore):
    new = []

    for v in l:
        if isinstance(v, list):
            new.append(fix_list_keys(v, convert_function))
        elif isinstance(v, dict):
            new.append(fix_dict_keys(v, convert_function))
        else:
            new.append(v)
    return new


def fix_dict_keys(d: dict, convert_function=to_underscore) -> dict:
    """
    Recursively change the naming convention of a dict's keys, returning as a new dict
    Modified from https://stackoverflow.com/a/33668421/4022104
    """

    new = {}
    for k, v in d.items():
        new_v = v

        if isinstance(v, dict):
            new_v = fix_dict_keys(v, convert_function)
        elif isinstance(v, list):
            new_v = fix_list_keys(v, convert_function)

        new[convert_function(k)] = new_v
    return new


def rename_key(d: dict, from_key: object, to_key: object):
    if from_key not in d:
        return

    d[to_key] = d[from_key]
    del d[from_key]


def replace_key(d: dict, key: str, func: callable):
    d[key] = func(d[key])


def str_to_datetime(value: str):
    if value:
        return arrow.get(value).datetime
    return None
