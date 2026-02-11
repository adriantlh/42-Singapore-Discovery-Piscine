#!/usr/bin/env python3

variable = [2,8,9,48,8,22,-12,2]
print (f"Original array: {variable}")
variable2 = set(variable)
var2 = []

for i in variable2:
    if i > 5:
        var2.append(i+2)
        
print(f"New Array: {var2}")

sets = set()

for i in var2:
    sets.add(str(i))

print (sets)

# --- Improvement Recommendations ---
# 1. Remove the space before parenthesis in print().
# 2. Add spaces after commas in the list.
# 3. Converting to a set (line 5) removes duplicate values and loses the original
#    order. If preserving order matters, use dict.fromkeys(variable) instead.
# 4. Converting integers to strings in the second set (line 17) seems unnecessary
#    unless string output is specifically required. The set would work fine with integers.
# 5. Sets are unordered — the output order is not guaranteed. If consistent
#    ordering is needed, use sorted() when printing.
# 6. Trailing whitespace on line 11 — remove it.
# 7. Use descriptive variable names: "variable2" -> "unique_numbers", "var2" -> "filtered".