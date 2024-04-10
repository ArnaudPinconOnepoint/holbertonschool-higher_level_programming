#!/usr/bin/python3
import sys

if __name__ == "__main__":
    no_arg = len(sys.argv)-1
    if no_arg == 0:
        print("0 arguments.")
    elif no_arg == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(no_arg))
    for i in range(no_arg - 1):
        print("{}: {}".format(i+1, sys.argv[i+1]))
