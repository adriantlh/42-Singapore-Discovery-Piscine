#!/usr/bin/env python3
import sys

i = int(input("Enter a number less than 25\n"))

if i > 25:
    print("Error")
    sys.exit()

while i <= 25:
    print(f"Inside the loop, my variable is {i}")
    i = i + 1
