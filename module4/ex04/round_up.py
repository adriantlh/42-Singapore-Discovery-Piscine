#!/usr/bin/env python3
import math

variable = float(input("Give me a number: "))

num = math.ceil(variable)

print (num)

# --- Improvement Recommendations ---
# 1. Remove the space before parenthesis in print().
# 2. Add a blank line after the import statement (PEP 8 convention).
# 3. The variable name "variable" is generic. Consider "user_number" or "value".
# 4. Similarly, "num" could be "rounded_up" to clarify the intent.
# 5. Consider showing the original value alongside the result for context:
#    print(f"{variable} rounded up is {num}")
# 6. Wrap float(input()) in try/except to handle non-numeric input.