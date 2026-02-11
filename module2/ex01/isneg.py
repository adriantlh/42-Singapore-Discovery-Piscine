#!/usr/bin/env python3


number = int(input())

if number > 0:
    print ("This number is positive")
if number < 0:
    print ("The number is negative")
if number == 0:
    print ("The number is both positive and negative")

# --- Improvement Recommendations ---
# 1. Remove the space before parenthesis in print() and int().
# 2. Use elif/else instead of three separate if statements. Since the conditions
#    are mutually exclusive, using elif avoids unnecessary checks:
#    if number > 0:
#        print("This number is positive")
#    elif number < 0:
#        print("The number is negative")
#    else:
#        print("The number is zero")
# 3. Mathematically, zero is neither positive nor negative (not "both").
#    Consider changing the message to: "The number is zero" or
#    "The number is neither positive nor negative".
# 4. The print messages are inconsistent: "This number" vs "The number". Pick one style.
# 5. Add a prompt message to input() so the user knows what to enter.