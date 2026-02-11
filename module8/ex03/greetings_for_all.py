#!/usr/bin/env python3

def greetings(x=None):
    if isinstance(x, int):
        print ('Error, It was not a name.')
    elif x is None:
        print ('Hello, noble stranger.')
    else:
        print (f'Hello, {x}.')


greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)

# --- Improvement Recommendations ---
# 1. Remove the space before parenthesis in print().
# 2. The isinstance(x, int) check on line 4 only catches integers, not floats or
#    other non-string types. A more robust approach is to check for strings:
#    if x is None:
#        print('Hello, noble stranger.')
#    elif isinstance(x, str):
#        print(f'Hello, {x}.')
#    else:
#        print('Error, It was not a name.')
# 3. Good use of default parameter value (x=None) for handling missing arguments.
# 4. Consider using if __name__ == "__main__": to guard the function calls.
