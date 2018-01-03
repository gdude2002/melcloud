# coding=utf-8
from inflection import underscore as to_underscore
__author__ = "Gareth Coles"


def fix_dict_keys(d):
    done = {}

    for k, v in d.items():
        k = to_underscore(k).lower()

        if isinstance(v, dict):
            done[k] = fix_dict_keys(v)
        else:
            done[k] = v

    return done
