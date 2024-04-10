#!/usr/bin/python3
import sys

if __name__ == "__main__":
    no_arg = len(sys.argv)-1
    res = 0
    for i in range(no_arg):
        res += int(sys.argv[i+1])
    print("{}".format(res, end=""))
