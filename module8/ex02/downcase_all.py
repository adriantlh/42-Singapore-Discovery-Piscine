#!/usr/bin/env python3

import sys

def downcase_it(x):
    word = x.lower()
    print (word)

i = 1

if len(sys.argv) ==1:
    print ("none")
else: 
    while i < len(sys.argv):
        downcase_it(sys.argv[i])
        i+=1

# --- Improvement Recommendations ---
# 1. Remove the space before parenthesis in print().
# 2. The function prints directly instead of returning a value. It's better practice
#    for functions to return values and let the caller decide what to do:
#    def downcase_it(x):
#        return x.lower()
# 3. Add spaces around == on line 11: len(sys.argv) == 1
# 4. Trailing whitespace on line 13: "else: " — remove it.
# 5. Add spaces around +=: i += 1
# 6. Use a for loop instead of while:
#    for arg in sys.argv[1:]:
#        print(arg.lower())