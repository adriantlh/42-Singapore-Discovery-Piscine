#!/usr/bin/env python3

first_number = int(input("Enter the first number:\n"))
second_number = int(input("Enter the second number:\n"))

ans = first_number * second_number
state = ""

if ans > 0:
    state = "positive"
if ans < 0: 
    state = "negative"
if ans == 0:
    state = "positive and negative"

print (f'{first_number} x {second_number} = {ans}')
print (f'The result is {state}')

# --- Improvement Recommendations ---
# 1. Remove the space before parenthesis in print() and int().
# 2. Use elif/else instead of three separate if statements (mutually exclusive conditions):
#    if ans > 0:
#        state = "positive"
#    elif ans < 0:
#        state = "negative"
#    else:
#        state = "zero"
# 3. Mathematically, zero is neither positive nor negative. Consider: state = "zero"
#    or state = "neither positive nor negative".
# 4. Trailing whitespace on line 11: "if ans < 0: " — remove the trailing space.
# 5. Wrap int(input()) in try/except to handle non-numeric input.

