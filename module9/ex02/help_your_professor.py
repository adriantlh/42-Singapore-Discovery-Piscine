#!/usr/bin/env python3

def average(x):
    count = len(x)
    score = sum(x.values())
    return (score/count)

class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
}

class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}

print (f"Average for class 3B: {average(class_3B)}.")
print (f"Average for class 3C: {average(class_3C)}.")

# --- Improvement Recommendations ---
# 1. Remove the space before parenthesis in print().
# 2. The parentheses in return (score/count) are unnecessary: return score / count
# 3. Add spaces around the / operator: score / count
# 4. Guard against division by zero if an empty dictionary is passed:
#    def average(x):
#        if not x:
#            return 0
#        return sum(x.values()) / len(x)
# 5. Consider rounding the result for cleaner output:
#    print(f"Average for class 3B: {average(class_3B):.2f}.")
# 6. Good use of sum() and len() built-in functions with dict.values().