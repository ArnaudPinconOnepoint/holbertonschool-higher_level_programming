#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    new_dic = a_dictionary.copy()
    best_val = 0
    best_student = None
    for k, v in new_dic.items():
        if v > best_val:
            best_val = v
            best_student = k
    return best_student
