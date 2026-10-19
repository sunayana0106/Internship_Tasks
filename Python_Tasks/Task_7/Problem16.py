# Problem 16- Caesar Cipher
# https://www.hackerrank.com/challenges/caesar-cipher-1/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def caesarCipher(s, k):
    encrypted = []
    # Normalize shift factor to stay within 0-25 range
    k = k % 26
    
    for char in s:
        if 'a' <= char <= 'z':
            # Shift lowercase letters
            base = ord('a')
            new_char = chr(base + (ord(char) - base + k) % 26)
            encrypted.append(new_char)
        elif 'A' <= char <= 'Z':
            # Shift uppercase letters
            base = ord('A')
            new_char = chr(base + (ord(char) - base + k) % 26)
            encrypted.append(new_char)
        else:
            # Leave symbols and numbers unchanged
            encrypted.append(char)
            
    return "".join(encrypted)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
