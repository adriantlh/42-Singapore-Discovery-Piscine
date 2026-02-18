#!/usr/bin/env python3

def is_integer_num(n):
    if isinstance(n, float):
        return n.is_integer()
    return False

variable = float(input("Give me a number: "))

if is_integer_num(variable):
    print("The number is an integer")
else:
    print("The number is a decimal")
