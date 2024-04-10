#!/usr/bin/python3
def list_arg(*argv):
    no_arg = len(argv)
    if no_arg == 0:
        print("0 arguments.")
    elif no_arg == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(no_arg))
    for i in range(no_arg):
        print("{}: {}".format(i+1, argv[i]))

""" if __name__ == "__main__":
    a = 10
    b = 5 """