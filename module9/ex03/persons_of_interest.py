#!/usr/bin/env python3

def famous_births(x):
    for i in x:
        print (f"{x[i]['name']} is a great scientist born in {x[i]['date_of_birth']}.")

women_scientists = {
    "ada": {"name": "Ada Lovelace", "date_of_birth": "1815"},
    "cecilia": {"name": "Cecila Payne", "date_of_birth": "1900"},
    "lise": {"name": "Lisa Meitner", "date_of_birth": "1878"},
    "grace": {"name": "Grace Hopper", "date_of_birth": "1906"},
}

famous_births(women_scientists)