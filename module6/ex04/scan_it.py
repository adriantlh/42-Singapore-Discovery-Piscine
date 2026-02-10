#!/usr/bin/env python3

import sys
import re 


if len(sys.argv) <= 2:
    print ("none")
else:
    searchterm = sys.argv[1]
    search_array = sys.argv[2]

    count = re.findall(searchterm, search_array)

    if len(count) == 0:
        print ("none")
    else:
        print (len(count))
