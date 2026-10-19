# Problem 15 -Game of Thrones - I
# https://www.hackerrank.com/challenges/game-of-thrones/problem


#!/bin/python3

import os
from collections import Counter

def gameOfThrones(s):
    freq = Counter(s)

    odd_count = sum(1 for count in freq.values() if count % 2 != 0)

    if odd_count <= 1:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input().strip()
    result = gameOfThrones(s)

    fptr.write(result + '\n')
    fptr.close()
