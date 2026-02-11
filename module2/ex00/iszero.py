#!/usr/bin/env python3

number = int(input())

if number != 0:
    print ("This number is different from zero")
else:
    print ("This number is equal to zero")

# --- Improvement Recommendations ---
# 1. Remove the space before parenthesis in print() and int().
# 2. Add a prompt message to input() so the user knows what to type:
#    number = int(input("Enter a number: "))
# 3. Wrap int(input()) in a try/except to handle non-numeric input:
#    try:
#        number = int(input("Enter a number: "))
#    except ValueError:
#        print("Please enter a valid integer.")