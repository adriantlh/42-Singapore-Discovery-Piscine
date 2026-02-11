#!/usr/bin/env python3

i = 0

while i < 11:
    j = 0
    string = ""
    while j < 11: 
        string += f"{i*j} "
        j += 1
    print (f"Table of {i}: {string}")
    i += 1

# --- Improvement Recommendations ---
# 1. Remove the space before parenthesis in print().
# 2. Trailing whitespace on line 8: "while j < 11: " — remove the trailing space.
# 3. Consider using for loops with range() instead of while loops:
#    for i in range(11):
#        row = " ".join(str(i * j) for j in range(11))
#        print(f"Table of {i}: {row}")
#    This is more Pythonic and eliminates manual counter management.
# 4. The trailing space in the string (f"{i*j} ") adds an extra space at the end
#    of each line. Using " ".join() as shown above avoids this.
# 5. The variable name "string" is generic. Consider "row" or "table_row".


