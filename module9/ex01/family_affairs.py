#!/usr/bin/env python3

# def find_the_redhead(x):
#     filtered_dict = [key for key, value in x.items() if value == "red" ]
#     return filtered_dict

def find_the_redhead(x):
    filtered = list (filter(lambda key: x[key] == "red" , x.keys() ))
    return filtered

dupont_family = {
    "florian" : "red",
    "marie": "blond",
    "virginie": "brunette",
    "david" : "red",
    "franck": "red"
}   

print (find_the_redhead(dupont_family))

#To print out only a list of the names
#print (list(dupont_family))

# --- Improvement Recommendations ---
# 1. Remove the space before parenthesis in print() and list().
# 2. Remove the commented-out alternative implementation (lines 3-5) or keep it with a
#    clear explanation of why. Dead commented-out code is confusing for readers.
# 3. The list comprehension version (commented out) is actually cleaner and more readable
#    than the lambda/filter approach. Consider using it as the main implementation:
#    def find_the_redhead(x):
#        return [key for key, value in x.items() if value == "red"]
# 4. Inconsistent spacing around colons in the dictionary:
#    "florian" : "red" vs "marie": "blond" — pick one style (no space before colon).
# 5. Trailing whitespace on line 17 — remove it.
# 6. Remove extra spaces in the filter call on line 8: list(filter(...))
