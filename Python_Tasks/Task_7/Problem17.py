# Problem 17 - Separate the Numbers
# https://www.hackerrank.com/challenges/separate-the-numbers/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'separateNumbers' function below.
# The function accepts STRING s as parameter.

def separateNumbers(s):
    # If the string starts with '0', it can never have a valid leading number without leading zeros
    if s.startswith('0'):
        print("NO")
        return

    n = len(s)
    # The first number can be at most half the length of the string
    for i in range(1, n // 2 + 1):
        first_str = s[:i]
        current_num = int(first_str)
        
        # Build the sequence starting from current_num
        built_string = first_str
        while len(built_string) < n:
            current_num += 1
            built_string += str(current_num)
            
        # Check if the generated string matches the input string
        if built_string == s:
            print(f"YES {first_str}")
            return

    print("NO")

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input().strip()
        separateNumbers(s)
