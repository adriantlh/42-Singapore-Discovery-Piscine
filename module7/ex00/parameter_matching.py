#!/usr/bin/env python3

import sys

if len(sys.argv) -1 != 1:
    print("none")
else:
    check = sys.argv[1]
    word = input("What was the parameter? ")
    if word == check:
        print('Good job!')
    else:
        print('Nope, sorry...')
