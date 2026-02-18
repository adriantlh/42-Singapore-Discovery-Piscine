#!/usr/bin/env python3

variable = [2,8,9,48,8,22,-12,2]
print(f"Original array: {variable}")
variable2 = set(variable)
var2 = []

for i in variable2:
    if i > 5:
        var2.append(i+2)

print(f"New Array: {var2}")

sets = set()

for i in var2:
    sets.add(str(i))

print(sets)
