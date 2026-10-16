# Problem 20- Piling Up!
# https://www.hackerrank.com/challenges/piling-up/problem

from collections import deque

def solve():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        blocks = deque(map(int, input().split()))
        
        # The first block placed can be anything, so start with infinity
        last_block = float('inf')
        possible = True
        
        while blocks:
            # Pick the larger of the two ends
            if blocks[0] >= blocks[-1]:
                current = blocks.popleft()
            else:
                current = blocks.pop()
                
            # The current block must be smaller than or equal to the last placed block
            if current <= last_block:
                last_block = current
            else:
                possible = False
                break
                
        if possible:
            print("Yes")
            else:
            print("No")

if __name__ == '__main__':
    solve()
