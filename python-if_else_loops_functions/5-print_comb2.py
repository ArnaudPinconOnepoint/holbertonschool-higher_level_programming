#!/usr/bin/python3
output = ""
for i in range(100):
    output += "{:02d}, ".format(i) if i != 99 else "{:02d}\n".format(i)
print(output, end='')
