#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value), end='\n')
        return True
    except TypeError as e:
        print('Exception: {}'.format(e), end="\n", file=sys.stderr)
        return False
    except ValueError as e:
        print('Exception: {}'.format(e), end="\n", file=sys.stderr)
        return False
