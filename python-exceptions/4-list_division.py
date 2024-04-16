#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = 0
    final_list = []
    try:
        for i in range(0, list_length):    
            res = my_list_1[i]/my_list_2[i]
            final_list.append(res)
    except TypeError:
        print("wrong type")
        final_list.append(0)
    except ZeroDivisionError:
        print("division by 0")
        final_list.append(0)
    except IndexError:
        print("out of range")
        final_list.append(0)
    finally:
        return final_list
