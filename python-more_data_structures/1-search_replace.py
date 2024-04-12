#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(map(lambda x: switch(x, search, replace), my_list))
    return new_list


def switch(x, search, replace):
    if x == search:
        return replace
    return x
