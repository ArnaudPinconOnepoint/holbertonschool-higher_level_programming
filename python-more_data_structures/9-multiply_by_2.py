#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for k, v in a_dictionary.items():
        a_dictionary.update({k: v*2})
    return a_dictionary
