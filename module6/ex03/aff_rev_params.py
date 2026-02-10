#!/usr/bin/env python3

import sys

Array = []

if len(sys.argv) != 3:
    print ("none")
else:
    i = 1
    while i < len(sys.argv): 
        Array.insert(0,sys.argv[i])
        i += 1


    for j in Array:
        print (j)