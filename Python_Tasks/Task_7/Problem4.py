# Problem 4- Funny String
https://www.hackerrank.com/challenges/funny-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'funnyString' function below.
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.

def funnyString(s):
    # Create the reverse of the string
    s_rev = s[::-1]
    
    # Compute the absolute differences between adjacent characters for both strings
    diffs = [abs(ord(s[i]) - ord(s[i-1])) for i in range(1, len(s))]
    diffs_rev = [abs(ord(s_rev[i]) - ord(s_rev[i-1])) for i in range(1, len(s_rev))]
    
    # Compare the lists
    if diffs == diffs_rev:
        return "Funny"
    else:
        return "Not Funny"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
