#!/usr/bin/env python3

import sys
import re

string = ""
searchterm = "z"
i = 1

if len(sys.argv) <= 1:
    print ("none")
else:

    while i < len(sys.argv):
        string += sys.argv[i]
        i += 1

    count = re.findall(searchterm,string)
    j = 0

    if len(count)  == 0:
        print ('none')
    else:
        while j < len(count):
            print (searchterm, end="")
            j+=1
        print ("")
        print (f"Count of z: {len(count)}")

# --- Improvement Recommendations ---
# 1. Remove the space before parenthesis in print().
# 2. The re (regex) module is overkill for counting a single character. Use str.count():
#    combined = "".join(sys.argv[1:])
#    count = combined.count("z")
#    This removes the need for the re import entirely.
# 3. The while loop to print each "z" individually (lines 24-26) can be replaced with:
#    print(searchterm * len(count))
# 4. Extra space on line 21: "if len(count)  == 0" — use single space.
# 5. Add a space after the comma on line 18: re.findall(searchterm, string)
# 6. Add spaces around += on line 26: j += 1