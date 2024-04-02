#!/usr/bin/python3
def print_last_digit(number):
    """prints and returns last digit."""
    last = number % 10
    if number < 0:
        last = 10 - last
    print('{0}'.format(last), end="")
    return last
