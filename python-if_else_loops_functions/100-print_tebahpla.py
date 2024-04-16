#!/usr/bin/python3
for i in reversed(range(ord('a'), ord('z') + 1)):
    print('{:s}'.format(chr(i).upper() if i % 2 == 1 else chr(i)), end='')
