# coding=utf-8
from inflection import underscore as to_underscore
__author__ = "Gareth Coles"


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
            new_v = list()

            for x in v:
                if isinstance(x, dict):
                    new_v.append(fix_dict_keys(x, convert_function))
                else:
                    new_v.append(x)

        new[convert_function(k)] = new_v
    return new


def rename_key(d: dict, from_key: object, to_key: object):
    d[to_key] = d[from_key]
    del d[from_key]
