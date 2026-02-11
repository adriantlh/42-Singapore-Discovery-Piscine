#!/usr/bin/env python3

i = int(input("Enter a number less than 25\n"))

if i > 25:
    print("Error")
    

while i <= 25:
    print (f"Inside the loop, my variable is {i}")
    i = i + 1

# --- Improvement Recommendations ---
# 1. Bug: If the user enters a number > 25, "Error" is printed but the while loop
#    is still reached (it just won't execute because i > 25). Add sys.exit() after
#    the error to stop execution, or use an else clause:
#    if i > 25:
#        print("Error")
#        sys.exit()
#    Or wrap the while loop inside an else block.
# 2. Remove the space before parenthesis in print().
# 3. Use i += 1 instead of i = i + 1 (more Pythonic).
# 4. Consider using a for loop: for i in range(start, 26): which is cleaner.
# 5. Wrap int(input()) in try/except to handle non-numeric input.

