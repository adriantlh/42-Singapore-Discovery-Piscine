#!/usr/bin/env python3

variable = [2,8,9,48,8,22,-12,2]
print (f"Original array: {variable}")

var2 = []

for i in variable:
    var2.append(i+2)

print(f"New Array: {var2}")

# --- Improvement Recommendations ---
# 1. Remove the space before parenthesis in the first print() (line 4).
#    Note: the second print on line 11 already follows PEP 8 — be consistent.
# 2. Add spaces after commas in the list: [2, 8, 9, 48, 8, 22, -12, 2]
# 3. Use a list comprehension instead of a loop with append — it's more Pythonic:
#    var2 = [i + 2 for i in variable]
# 4. Use descriptive variable names: "variable" -> "numbers", "var2" -> "incremented".