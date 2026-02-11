#!/usr/bin/env python3

variable = input("Enter your string!")

va2 = ""

for i in variable:
    if i.islower():
        va2 += i.upper()
    elif i.isupper():
        va2 += i.lower()
    else:
        va2 += i
    

print (va2)

# --- Improvement Recommendations ---
# 1. Remove the space before parenthesis in print().
# 2. The variable name "va2" is unclear. Consider "swapped" or "result".
# 3. Python has a built-in method that does exactly this: str.swapcase()
#    You can replace the entire loop with: print(variable.swapcase())
# 4. Trailing whitespace on line 14 — remove it.
# 5. Building strings with += in a loop is O(n^2) in the worst case. For large strings,
#    consider using a list and "".join() instead:
#    result = [c.upper() if c.islower() else c.lower() if c.isupper() else c for c in variable]
#    print("".join(result))

