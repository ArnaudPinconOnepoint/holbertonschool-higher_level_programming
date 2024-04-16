#!/usr/bin/python3
def weight_average(my_list=[]):
    top = 0
    bottom = 0
    if len(my_list) == 0:
        return 0
    for i in range (my_list):
        top=top+i.get(0)*i.get(1)
        bottom=bottom+i.get(1)
    return top/bottom
