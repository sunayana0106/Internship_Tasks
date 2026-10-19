# Problem 9- Beautiful Binary String
# https://www.hackerrank.com/challenges/beautiful-binary-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulBinaryString' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING b as parameter.
#

def beautifulBinaryString(b):
    # Write your code here
    count = 0
    i = 0
    n = len(b)
    
    # Convert string to a list since strings are immutable in Python
    b = list(b)
    
    while i <= n - 3:
        if b[i] == '0' and b[i+1] == '1' and b[i+2] == '0':
            # Change the third character to break the '010' pattern
            b[i+2] = '1'
            count += 1
            i += 3  # Skip past this pattern
        else:
            i += 1
            
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()
