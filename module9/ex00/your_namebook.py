#!/usr/bin/env python3

def array_of_names(x):
    for i,j in x.items():
      print (f"{i.title()} {j.title()}")


persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindcier"
}

array_of_names(persons)

# --- Improvement Recommendations ---
# 1. Remove the space before parenthesis in print().
# 2. Inconsistent indentation: line 5 uses 2 spaces, but PEP 8 recommends 4 spaces.
#    Use consistent 4-space indentation throughout.
# 3. The function name "array_of_names" is misleading — it takes a dictionary and prints,
#    not an array. Consider "print_names" or "display_namebook".
# 4. Use more descriptive loop variable names. Instead of i,j use first_name, last_name:
#    for first_name, last_name in x.items():
#        print(f"{first_name.title()} {last_name.title()}")
# 5. Add a space after the comma on line 4: for i, j in x.items()