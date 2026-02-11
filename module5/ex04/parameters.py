#!/usr/bin/env python3

import sys

print ("Number of parameters:", len(sys.argv)-1)

# --- Improvement Recommendations ---
# 1. Remove the space before parenthesis in print().
# 2. Add spaces around the - operator for readability: len(sys.argv) - 1
# 3. Consider using an f-string for consistency:
#    print(f"Number of parameters: {len(sys.argv) - 1}")