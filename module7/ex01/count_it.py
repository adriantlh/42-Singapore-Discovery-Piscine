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

# --- Improvement Recommendations ---
# 1. Remove the space before parenthesis in print().
# 2. PEP 8: variable names should be lowercase. Rename "Array" to "args" or "params".
# 3. The "i = 1" on line 10 is immediately overwritten by the for loop — remove it.
# 4. The "i += 1" on line 13 is unnecessary inside a for loop. The for loop
#    handles iteration automatically — this increment is overwritten each iteration.
# 5. Trailing whitespace on line 11 — remove it.
# 6. The Array is just a copy of sys.argv[1:]. Simplify by using slicing directly:
#    args = sys.argv[1:]
#    print(f'parameters: {len(args)}')
#    for arg in args:
#        print(f'{arg}: {len(arg)}')