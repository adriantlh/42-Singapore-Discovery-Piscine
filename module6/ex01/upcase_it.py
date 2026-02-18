#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("none")
else:
    i = 1
    words = ""
    while i < len(sys.argv):
        words += sys.argv[i].upper()
        if i != len(sys.argv) - 1:
            words += " "
        i += 1
    print(words)
