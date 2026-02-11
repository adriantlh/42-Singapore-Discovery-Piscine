#!/usr/bin/env python3

def upcase_it(x):
    word = x.upper()
    return word

print(upcase_it("hello"))

# --- Improvement Recommendations ---
# 1. Good job — this file already follows PEP 8 for print() (no space before parens).
# 2. The function can be simplified to a one-liner:
#    def upcase_it(x):
#        return x.upper()
#    The intermediate variable "word" is not needed.
# 3. Consider using a more descriptive parameter name: "text" or "string" instead of "x".