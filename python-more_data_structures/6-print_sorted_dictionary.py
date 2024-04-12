#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dic = dict(sorted(a_dictionary.items()))
    for k, v in new_dic.items():
        print('{}: {}'.format(k, v, end="\n"))
