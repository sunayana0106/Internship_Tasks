# Problem 1- Python If-Else
# https://www.hackerrank.com/challenges/py-if-else/problem

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print("Weird")
    # Check if n is even
    else:
        # If n is even and in the inclusive range of 2 to 5
        if 2 <= n <= 5:
            print("Not Weird")
        # If n is even and in the inclusive range of 6 to 20
        elif 6 <= n <= 20:
            print("Weird")
        # If n is even and greater than 20
        elif n > 20:
            print("Not Weird")
