# Problem 6- Pangrams
# https://www.hackerrank.com/challenges/pangrams/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    unique_letters = set(char for char in s.lower() if char.isalpha())
    
    # Check if all 26 letters are present
    if len(unique_letters) == 26:
        return "pangram"
    else:
        return "not pangram"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
