#!/usr/bin/env python3

def add_one(x):
    x += 1
    return x

number = 1
print(number)

add_one(number)
print(number)

number = add_one(number)
print(number)
