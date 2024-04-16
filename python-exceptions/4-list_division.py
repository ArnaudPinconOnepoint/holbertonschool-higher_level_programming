#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = 0
    try:
        if (len(my_list_1) != len(my_list_2)):
            return print("out of range")
        for i in range(len(my_list_1)):    
            res = my_list_1[i]/my_list_2[i]
            if res is None: res = 0
            list_length.append(res)
    except TypeError:
        return print("wrong type")
    except ZeroDivisionError:
        return print("division by 0")
    finally:
        return print("{}".format(list_length), end="")
