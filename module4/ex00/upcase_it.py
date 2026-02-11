#!/usr/bin/env python3

words = input("Give me a word: ")

uped = words.upper()

print (f"{uped}")

# --- Improvement Recommendations ---
# 1. Remove the space before parenthesis in print() and input().
# 2. print(f"{uped}") is redundant — the f-string adds no value here.
#    Simply use: print(uped)
# 3. You could simplify the entire script to:
#    print(input("Give me a word: ").upper())
# 4. The variable name "uped" is unclear. Consider "uppercased" or "upper_word".