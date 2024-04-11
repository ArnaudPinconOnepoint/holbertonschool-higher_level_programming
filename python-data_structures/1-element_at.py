#!/usr/bin/python3
def print_list_integer(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    print("Element at index {:d} is {:d}".format(idx, my_list[idx]))
