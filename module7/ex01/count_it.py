#!/usr/bin/env python3

import sys

Array = []

if len(sys.argv) <= 1:
    print ("none")
else:
    i = 1
    for i in range(1, len(sys.argv)): 
        Array.append(sys.argv[i])
        i += 1
    print (f'parameters: {len(Array)}')
    for j in Array:
        print (f'{j}: {len(j)}')