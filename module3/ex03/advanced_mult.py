#!/usr/bin/env python3

i = 0

while i < 11:
    j = 0
    string = ""
    while j < 11:
        string += f"{i*j} "
        j += 1
    print(f"Table of {i}: {string}")
    i += 1
