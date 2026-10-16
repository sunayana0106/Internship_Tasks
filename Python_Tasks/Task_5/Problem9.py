# Problem 9- Word Order
# https://www.hackerrank.com/challenges/word-order/problem

from collections import defaultdict
import sys

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    n = int(input_data[0])
    words = input_data[1:n+1]
    
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
        
    print(len(counts))
    print(*(counts.values()))

if __name__ == '__main__':
    solve()
