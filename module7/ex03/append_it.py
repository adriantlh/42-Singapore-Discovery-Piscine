#!/usr/bin/env python3

import sys

phrase = sys.argv
array = []
i = 1
j = 0
if len(sys.argv) <= 1:
    print ("none")
else:
    while i < len(sys.argv):
        if sys.argv[i][-3:] != "ism":
            array.append(sys.argv[i]+"ism")
        i += 1
    while j < len(array):
        print (array[j])
        j+=1

# --- Improvement Recommendations ---
# 1. Remove the space before parenthesis in print().
# 2. The variable "phrase" on line 5 is assigned but never used — remove it.
# 3. The while loops can be replaced with for loops for cleaner code:
#    for arg in sys.argv[1:]:
#        if not arg.endswith("ism"):
#            array.append(arg + "ism")
#    for item in array:
#        print(item)
# 4. Use str.endswith("ism") instead of string slicing [-3:] != "ism" — more readable.
# 5. Add spaces around += on line 18: j += 1
# 6. Could use a list comprehension:
#    result = [arg + "ism" for arg in sys.argv[1:] if not arg.endswith("ism")]
