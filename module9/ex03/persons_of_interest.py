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