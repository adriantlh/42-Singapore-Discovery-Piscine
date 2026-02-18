#!/usr/bin/env python3

def array_of_names(x):
    for i,j in x.items():
      print(f"{i.title()} {j.title()}")


persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindcier"
}

array_of_names(persons)
