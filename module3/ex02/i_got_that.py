#!/usr/bin/env python3

stopword = "STOP"


while True:
    word = input("I got that! Anything else? : ")
    if word == stopword:
        break

# --- Improvement Recommendations ---
# 1. Consider making the comparison case-insensitive so "stop", "Stop", etc. all work:
#    if word.upper() == stopword:
# 2. Add a farewell message after the loop ends, e.g.:
#    print("Goodbye!")
# 3. The initial prompt "I got that! Anything else?" is misleading on the first
#    iteration since nothing has been "got" yet. Consider using a different prompt
#    for the first input vs subsequent ones.