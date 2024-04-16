#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dic = a_dictionary.copy()
    for i in a_dictionary.keys():
        if a_dictionary.get(i) == value:
            new_dic.pop(i)
    return new_dic
