#!/usr/bin/python3
def number_keys(a_dictionary):
    nbKey = len(list(dict.fromkeys(a_dictionary)))
    return nbKey
