#!/usr/bin/env python3

def hello():
    print ('Hello, everyone!')

hello()

# --- Improvement Recommendations ---
# 1. Remove the space before parenthesis in print().
# 2. Good practice: wrap the function call in an if __name__ == "__main__": guard.
#    This prevents the function from running when the file is imported as a module:
#    if __name__ == "__main__":
#        hello()