# Problem 14 - Anagram
# https://www.hackerrank.com/challenges/anagram/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def anagram(s):
    n = len(s)

    # Odd-length strings cannot be split into equal halves
    if n % 2 != 0:
        return -1

    mid = n // 2
    s1 = s[:mid]
    s2 = s[mid:]

    c1 = Counter(s1)
    c2 = Counter(s2)

    changes = 0

    for char, count in c1.items():
        if count > c2[char]:
            changes += count - c2[char]

    return changes


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()
        result = anagram(s)
        fptr.write(str(result) + '\n')

    fptr.close()
