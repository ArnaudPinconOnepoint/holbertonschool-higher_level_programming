#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = a_dictionary
    for k, v in new_dic.items():
        new_dic.update({k: v*2})
    return new_dic
