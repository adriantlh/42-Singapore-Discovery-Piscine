#!/usr/bin/env python3

first = int(input("Give me the first number: "))
second = int(input("Give me the second number: "))

print ("Thank you!")

print (f"{first} + {second} = {first + second}")
print (f"{first} - {second} = {first - second}")
print (f"{first} / {second} = {int(first / second)}")
print (f"{first} * {second} = {first * second}")

# --- Improvement Recommendations ---
# 1. Remove the space before parenthesis in print() and int().
# 2. Bug: Division by zero is not handled. If second == 0, the division line
#    will raise a ZeroDivisionError. Add a check:
#    if second != 0:
#        print(f"{first} / {second} = {first // second}")
#    else:
#        print(f"{first} / {second} = undefined (division by zero)")
# 3. Use integer division operator // instead of int(first / second).
#    int(first / second) does float division then truncates; // does true floor division.
#    Example: int(-7 / 2) = -3, but -7 // 2 = -4. The // operator is more correct.
# 4. Wrap int(input()) in try/except to handle non-numeric input.
