# Problem 20 - No Idea!
# https://www.hackerrank.com/challenges/no-idea/problem

import sys

def solve():
    # Read all inputs from standard input efficiently
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Array elements
    arr = input_data[2:2+n]
    
    # Sets A and B using integer conversion for fast lookup
    A = set(input_data[2+n : 2+n+m])
    B = set(input_data[2+n+m:])
    
    # Calculate happiness
    # Using a generator expression with sum
    happiness = sum((1 if x in A else -1 if x in B else 0) for x in arr)
    
    print(happiness)

if __name__ == '__main__':
    solve()
