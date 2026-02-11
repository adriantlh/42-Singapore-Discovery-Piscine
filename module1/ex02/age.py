my_age = int(input('what is your age?'))

age42 = my_age + 42

print (age42)

# --- Improvement Recommendations ---
# 1. Add a shebang line at the top: #!/usr/bin/env python3
# 2. Remove the space before parenthesis in print().
# 3. Wrap int(input(...)) in a try/except to handle non-numeric input gracefully:
#    try:
#        my_age = int(input('What is your age? '))
#    except ValueError:
#        print("Please enter a valid number.")
# 4. The variable name "age42" is unclear. Consider "age_plus_42" or "future_age"
#    to make the intent more obvious.
# 5. Add a space after the question mark in the prompt for readability: 'What is your age? '