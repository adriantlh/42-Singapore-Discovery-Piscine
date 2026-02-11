#!/usr/bin/env python3

import sys

def shrink(x):
    print(x[0:8])

def enlarge(x):
    print(x + (8-len(x)) * "z")

i = 1

if len(sys.argv) == 1:
    print ("none")
else:
    while i < len(sys.argv):
        if len(sys.argv[i]) <= 8:
            enlarge(sys.argv[i])
        else:
            shrink(sys.argv[i])
        i+=1
