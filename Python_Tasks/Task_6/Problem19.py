# Problem 19 -Company Logo
# https://www.hackerrank.com/challenges/most-commons/problem


#!/bin/python3

from collections import Counter

if __name__ == '__main__':
    s = input().strip()
    frequency = Counter(s)

    sorted_chars = sorted(
        frequency.items(),
        key=lambda x: (-x[1], x[0])
    )

    for char, count in sorted_chars[:3]:
        print(char, count)
