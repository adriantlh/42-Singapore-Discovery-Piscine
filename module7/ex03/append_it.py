#!/usr/bin/env python3

import sys

array = []
i = 1
j = 0
if len(sys.argv) <= 1:
    print("none")
else:
    while i < len(sys.argv):
        if sys.argv[i][-3:] != "ism":
            array.append(sys.argv[i]+"ism")
        i += 1
    while j < len(array):
        print(array[j])
        j += 1
