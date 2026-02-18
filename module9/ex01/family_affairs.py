#!/usr/bin/env python3

def find_the_redhead(x):
    filtered = list(filter(lambda key: x[key] == "red", x.keys()))
    return filtered

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redhead(dupont_family))
