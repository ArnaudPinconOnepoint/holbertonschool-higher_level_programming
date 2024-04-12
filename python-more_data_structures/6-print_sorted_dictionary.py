#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dic = dict(sorted(a_dictionary.items()))
    list(map(lambda x: print(x, end='\n'), new_dic.items()))
