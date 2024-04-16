#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = 0
    try:
        for i in range(len(my_list_1)):    
            res = my_list_1[i]/my_list_2[i]
            list_length.append(res)
    except TypeError:
        print("wrong type")
        list_length.append(0)
    except ZeroDivisionError:
        print("division by 0")
        list_length.append(0)
    except IndexError:
        print("out of range")
        list_length.append(0)
    finally:
        print("{}".format(list_length), end="")
