#!/usr/bin/env python3

variable = [2,8,9,48,8,22,-12,2]
print (f"Original array: {variable}")

var2 = []

for i in variable:
    if i > 5:
        var2.append(i+2)

print(f"New Array: {var2}")

# --- Improvement Recommendations ---
# 1. Remove the space before parenthesis in the first print().
# 2. Add spaces after commas in the list.
# 3. Use a list comprehension — cleaner and more Pythonic:
#    var2 = [i + 2 for i in variable if i > 5]
# 4. Use descriptive variable names: "variable" -> "numbers", "var2" -> "filtered".