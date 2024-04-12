#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_dict = {}
    for i in my_list:
        my_dict.setdefault(i, i)
    return sum(my_dict.values())


# other solution
#mylist = ["a", "b", "a", "c", "c"]
#mylist = list(dict.fromkeys(mylist))
#print(mylist)