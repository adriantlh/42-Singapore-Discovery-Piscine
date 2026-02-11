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

# --- Improvement Recommendations ---
# 1. Remove the space before parenthesis in print().
# 2. Trailing whitespace on line 4: "import re " — remove it.
# 3. The re (regex) module is overkill here. Use the built-in str.count() method:
#    count = search_array.count(searchterm)
#    This is simpler, faster, and doesn't require an import.
# 4. With str.count(), you can simplify the check:
#    count = sys.argv[2].count(sys.argv[1])
#    print(count if count > 0 else "none")
