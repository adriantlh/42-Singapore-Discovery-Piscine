#!/usr/bin/env python3

import sys

n = len(sys.argv)



if len(sys.argv) != 2:
    print ("none")
else:
    i = 1
    words = ""
    while i < len(sys.argv):
        words+=sys.argv[i].upper()
        if i != len(sys.argv)-1:
            words+=" "
        i+=1
    print (words)

# --- Improvement Recommendations ---
# 1. Remove the space before parenthesis in print().
# 2. The variable "n" on line 5 is assigned but never used — remove it.
# 3. Extra blank lines (lines 6-8) — reduce to one blank line.
# 4. Add spaces around += operators: words += sys.argv[i].upper()
# 5. Since only 1 parameter is expected (len == 2), the while loop and space-joining
#    logic is unnecessary. You can simplify to:
#    print(sys.argv[1].upper())
# 6. For multiple args, use " ".join() instead of manual concatenation:
#    print(" ".join(arg.upper() for arg in sys.argv[1:]))

