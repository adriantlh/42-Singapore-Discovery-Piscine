#!/usr/bin/env python3

import sys

print (sys.argv[1])

# --- Improvement Recommendations ---
# 1. Remove the space before parenthesis in print().
# 2. Bug: No bounds checking — if no arguments are provided, sys.argv[1] will raise
#    an IndexError. Add a guard:
#    if len(sys.argv) > 1:
#        print(sys.argv[1])
#    else:
#        print("No parameter provided")