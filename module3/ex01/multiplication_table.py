#!/usr/bin/env python3

number = int(input('Enter a number\n'))

i = 0

while i < 10:
    print (f"{i} x {number} = {i*number}")
    i = i+1

# --- Improvement Recommendations ---
# 1. Remove the space before parenthesis in print().
# 2. Use i += 1 instead of i = i+1 (more Pythonic), and add spaces around +=.
# 3. Consider using a for loop with range() instead of a while loop:
#    for i in range(10):
#        print(f"{i} x {number} = {i * number}")
#    This eliminates the need for manual counter management.
# 4. The table only goes from 0 to 9. Consider going up to 10 or 12 for a
#    complete multiplication table.
# 5. Wrap int(input()) in try/except to handle non-numeric input.

