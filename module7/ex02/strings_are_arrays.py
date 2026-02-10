#!/usr/bin/env python3

import sys
import re

string = ""
searchterm = "z"
i = 1

if len(sys.argv) <= 1:
    print ("none")
else:

    while i < len(sys.argv):
        string += sys.argv[i]
        i += 1

    count = re.findall(searchterm,string)
    j = 0

    if len(count)  == 0:
        print ('none')
    else:
        while j < len(count):
            print (searchterm, end="")
            j+=1
        print ("")
        print (f"Count of z: {len(count)}")