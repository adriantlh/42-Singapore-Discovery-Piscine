#!/usr/bin/env python3

import sys

Array = []

if len(sys.argv) <= 1:
    print("none")
else:
    for i in range(1, len(sys.argv)):
        Array.append(sys.argv[i])
    print(f'parameters: {len(Array)}')
    for j in Array:
        print(f'{j}: {len(j)}')
