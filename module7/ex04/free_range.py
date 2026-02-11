#!/usr/bin/env python3

import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

array =[]

if len(sys.argv) !=3:
    print ("none")
else:
    if num1 > num2:
        print('error, num2 must be bigger than num1')
    else:
        while num1 < num2+1:
            array.append(num1)
            num1 += 1
    print (array)

# --- Improvement Recommendations ---
# 1. Remove the space before parenthesis in print().
# 2. Bug: Lines 5-6 access sys.argv[1] and sys.argv[2] BEFORE checking len(sys.argv)
#    on line 10. If fewer than 3 args are provided, this crashes with IndexError.
#    Move the length check to the top, before accessing sys.argv.
# 3. Add a space before the opening bracket: array = [] not array =[]
# 4. Add spaces around !=: len(sys.argv) != 3
# 5. The while loop can be replaced with the built-in range() function:
#    array = list(range(num1, num2 + 1))
#    This is a one-liner that does the same thing.
# 6. Wrap int() calls in try/except to handle non-numeric arguments.