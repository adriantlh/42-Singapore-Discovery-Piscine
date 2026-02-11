#!/usr/bin/env python3

variable = float(input("Give me a number: "))

def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False

if is_integer_num(variable):
    print ("The number is an integer")
else:
    print ("The number is a decimal")

# --- Improvement Recommendations ---
# 1. Remove the space before parenthesis in print().
# 2. Logic issue: Since variable is always assigned via float(input(...)), it will
#    ALWAYS be a float type. The isinstance(n, int) check on line 6 will never be True.
#    The function still works because it falls through to the n.is_integer() check,
#    but the int branch is dead code.
# 3. Define the function before using it (move it above the input line) for better
#    code organization. Placing function definitions at the top is a common convention.
# 4. Wrap float(input()) in try/except to handle non-numeric input.