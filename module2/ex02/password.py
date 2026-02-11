#!/usr/bin/env python3

password = input("Enter your password\n")

passcode =  "password2"

if password == passcode:
	print ("ACCESS GRANTED")
else:
	print ("ACCESS DENIED")

# --- Improvement Recommendations ---
# 1. Use consistent indentation: the if/else block uses tabs, but PEP 8 recommends 4 spaces.
#    Mixing tabs and spaces can cause IndentationError in Python 3.
# 2. Remove the extra space in: passcode =  "password2"  (double space after =).
# 3. Remove the space before parenthesis in print() and input().
# 4. Security: hardcoding passwords in source code is a bad practice. In real applications,
#    use environment variables, config files, or hashed password comparison.
# 5. Consider using getpass.getpass() instead of input() to hide password input:
#    from getpass import getpass
#    password = getpass("Enter your password: ")
