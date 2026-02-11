#!/usr/bin/env python3

import sys

Array = []

if len(sys.argv) != 3:
    print ("none")
else:
    i = 1
    while i < len(sys.argv): 
        Array.insert(0,sys.argv[i])
        i += 1


    for j in Array:
        print (j)

# --- Improvement Recommendations ---
# 1. Remove the space before parenthesis in print().
# 2. PEP 8: variable names should be lowercase. Rename "Array" to "array" or "reversed_args".
# 3. Trailing whitespace on line 11: "while i < len(sys.argv): " — remove it.
# 4. Add a space after the comma: Array.insert(0, sys.argv[i])
# 5. Much simpler approach using slicing to reverse:
#    for arg in reversed(sys.argv[1:]):
#        print(arg)
#    Or: for arg in sys.argv[1:][::-1]:  print(arg)