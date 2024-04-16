#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = 0
    try:
        if (len(my_list_1) != len(my_list_2)):
            print("out of range")
        for i in range(len(my_list_1)):    
            res = my_list_1[i]/my_list_2[i]
            if res is None: res = 0
            list_length.append(res)
    except TypeError:
        print("wrong type")
    except ZeroDivisionError:
        print("division by 0")
    finally:
        print("{}".format(list_length), end="")
