#!/usr/bin/env python3

variable = float(input("Give me a number: "))

def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False

if is_integer_num(variable):
    print ("The number is an integer")
else:
    print ("The number is a decimal")