#!/usr/bin/env python3

age = int(input("Please tell me your age: "))

print (f"You are currently {age} years old.")

i = 10

while i < 31:
    print (f"In {i} years, you'll be {i + age} years old.")
    i += 10

# --- Improvement Recommendations ---
# 1. Remove the space before parenthesis in print() and int().
# 2. Replace the while loop with a for loop using range() for clarity:
#    for years in range(10, 31, 10):
#        print(f"In {years} years, you'll be {years + age} years old.")
# 3. Wrap int(input()) in try/except to handle non-numeric input.
# 4. Consider validating that age is a positive number.
