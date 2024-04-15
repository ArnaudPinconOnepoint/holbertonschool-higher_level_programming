#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    #number of digits returned
    nb = 0
    try:
        for i in range (0, x):
            print("{}".format(my_list[i]), end="")
            nb +=1
        return nb
    except IndexError:
        return nb
