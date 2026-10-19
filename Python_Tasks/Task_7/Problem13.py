# Problem 13 - Sherlock and the Valid String
# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem


#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def isValid(s):
    freq = Counter(s)
    counts = Counter(freq.values())

    # All characters have the same frequency
    if len(counts) == 1:
        return "YES"

    # More than two distinct frequencies
    if len(counts) > 2:
        return "NO"

    f1, f2 = sorted(counts.keys())
    c1, c2 = counts[f1], counts[f2]

    # One character occurs only once
    if f1 == 1 and c1 == 1:
        return "YES"

    # One character occurs one extra time
    if f2 - f1 == 1 and c2 == 1:
        return "YES"

    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    result = isValid(s)

    fptr.write(result + '\n')
    fptr.close()
