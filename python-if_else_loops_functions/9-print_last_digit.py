#!/usr/bin/python3
def print_last_digit(number):
    l_digit = abs(number) % 10
    print(l_digit, end="")
    return (l_digit)
print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)