#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(args)
    except TypeError as e:
        print('Exception: {}'.format(e), end="\n", file=sys.stderr)
        res = None
    finally:
        return res
