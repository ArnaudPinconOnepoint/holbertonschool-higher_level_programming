#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return str
    new_res = str[:n] + str[n+1:]
    return new_res
