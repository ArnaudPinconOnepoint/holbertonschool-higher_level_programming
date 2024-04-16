#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
    except TypeError as e:
        print('Exception: {}'.format(e), end="\n", file=sys.stderr)
        res = None
    except ValueError as e:
        print('Exception: {}'.format(e), end="\n", file=sys.stderr)
        res = None
    except ZeroDivisionError as e:
        print('Exception: {}'.format(e), end="\n", file=sys.stderr)
        res = None
    except NameError as e:
        print('Exception: {}'.format(e), end="\n", file=sys.stderr)
        res = None
    except IndexError as e:
        print('Exception: {}'.format(e), end="\n", file=sys.stderr)
        res = None
    finally:
        return res
