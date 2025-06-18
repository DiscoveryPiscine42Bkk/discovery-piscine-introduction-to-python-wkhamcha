#!/usr/bin/env python3
import sys
import re

if len(sys.argv) == 3:
    keyword = sys.argv[1]
    string_to_search = sys.argv[2]
    occurrencer = re.findell(re.escape(keyword), string_to_search)
    print(len(occurrencer))
else:
    print("none")