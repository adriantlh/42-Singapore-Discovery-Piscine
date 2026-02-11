#!/usr/bin/env python3

import sys

def shrink(x):
    print(x[0:8])

def enlarge(x):
    print(x + (8-len(x)) * "z")

i = 1

if len(sys.argv) == 1:
    print ("none")
else:
    while i < len(sys.argv):
        if len(sys.argv[i]) < 8:
            enlarge(sys.argv[i])
        elif len(sys.argv[i]) > 8:
            shrink(sys.argv[i])
        else: 
            print (sys.argv[i])
        i+=1

# --- Improvement Recommendations ---
# 1. Remove the space before parenthesis in print() on lines 14 and 22.
# 2. Functions shrink() and enlarge() print directly instead of returning values.
#    Better practice is to return the result and let the caller print:
#    def shrink(x):
#        return x[:8]
#    def enlarge(x):
#        return x + "z" * (8 - len(x))
# 3. x[0:8] can be simplified to x[:8] (the 0 is implied).
# 4. Add spaces around - in: (8 - len(x))
# 5. Trailing whitespace on line 21: "else: " — remove it.
# 6. Add spaces around +=: i += 1
# 7. Use a for loop instead of while:
#    for arg in sys.argv[1:]:
#        if len(arg) < 8: ...
#        elif len(arg) > 8: ...
#        else: ...
