#!/usr/bin/python3
def uppercase(str):
    str_up = ""
    for i in str:
        if 'a' <= i <= 'z':
            i = chr(ord(i) - 32)
        str_up += i
    print(str_up)
