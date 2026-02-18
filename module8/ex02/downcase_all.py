#!/usr/bin/env python3

import sys

def downcase_it(x):
    word = x.lower()
    print(word)

i = 1

if len(sys.argv) == 1:
    print("none")
else:
    while i < len(sys.argv):
        downcase_it(sys.argv[i])
        i += 1
