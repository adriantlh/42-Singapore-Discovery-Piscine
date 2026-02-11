#!/usr/bin/env python3

import sys

if len(sys.argv) -1 != 1:
    print ("none")
else:
    check = sys.argv[1]
    word = input("What was the parameter? ")
    if word == check:
        print ('Good job!')
    else:
        print ('Nope, sorry...')

# --- Improvement Recommendations ---
# 1. Remove the space before parenthesis in print().
# 2. Simplify the condition: len(sys.argv) -1 != 1 is the same as len(sys.argv) != 2.
#    The current form is harder to read. Use: if len(sys.argv) != 2:
# 3. Add spaces around operators: len(sys.argv) - 1 (PEP 8).
# 4. Use consistent quote style — the file mixes single and double quotes.
