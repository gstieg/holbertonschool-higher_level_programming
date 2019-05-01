#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            c = ord(i) - 32
        else:
            c = ord(i)
        print(chr(c), end="")
    print()
