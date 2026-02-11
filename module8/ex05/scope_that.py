#!/usr/bin/env python3

def add_one(x):
    x +=1
    return x

number = 1
print (number)

add_one(number)
print (number)

number = add_one(number)
print (number)

# --- Improvement Recommendations ---
# 1. Remove the space before parenthesis in print().
# 2. Add spaces around += in the function: x += 1 (line 4).
# 3. Line 10: add_one(number) is called but the return value is discarded. This is
#    intentional to demonstrate scope (number stays 1), but a comment explaining
#    this would help readers understand it's deliberate:
#    add_one(number)  # return value discarded — number is unchanged (demonstrates scope)
# 4. Good demonstration of Python's scope rules. Integers are immutable, so x += 1
#    creates a new local variable inside the function without affecting the outer "number".