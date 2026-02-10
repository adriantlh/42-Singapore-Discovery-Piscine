#!/usr/bin/env python3

variable = input("Enter your string!")

va2 = ""

for i in variable:
    if i.islower():
        va2 += i.upper()
    elif i.isupper():
        va2 += i.lower()
    else:
        va2 += i
    

print (va2)

