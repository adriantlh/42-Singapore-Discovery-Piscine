#!/usr/bin/env python3

def famous_births(x):
    x = sorted(x.items(), key=lambda item: item[1]["date_of_birth"])
    x = dict(x)
    for i in x:
        print (f"{x[i]['name']} is a great scientist born in {x[i]['date_of_birth']}.")

women_scientists = {
    "ada": {"name": "Ada Lovelace", "date_of_birth": "1815"},
    "cecilia": {"name": "Cecilia Payne", "date_of_birth": "1900"},
    "lise": {"name": "Lise Meitner", "date_of_birth": "1878"},
    "grace": {"name": "Grace Hopper", "date_of_birth": "1906"},
}

famous_births(women_scientists)

# --- Improvement Recommendations ---
# 1. Remove the space before parenthesis in print().
# 2. Typos in the data:
#    - "Cecila Payne" should be "Cecilia Payne" (missing 'i')
#    - "Lisa Meitner" should be "Lise Meitner" (her name was Lise, not Lisa)
# 3. Use .items() to iterate over both key and value, which is cleaner:
#    def famous_births(x):
#        for key, info in x.items():
#            print(f"{info['name']} is a great scientist born in {info['date_of_birth']}.")
# 4. The loop variable "i" iterates over dictionary keys. Using a descriptive name
#    like "key" or "scientist" improves readability.
# 5. Consider using a more descriptive parameter name: "scientists" instead of "x".