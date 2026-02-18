#!/usr/bin/env python3

import sys

array = []

if len(sys.argv) != 3:
    print("none")
else:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    if num1 > num2:
        print('error, num2 must be bigger than num1')
    else:
        while num1 < num2 + 1:
            array.append(num1)
            num1 += 1
    print(array)
