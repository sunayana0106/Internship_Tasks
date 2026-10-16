# Problem 17- No Idea!
# https://www.hackerrank.com/challenges/no-idea/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def solve():
    # Read all inputs from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Elements of the array
    arr = input_data[2:2+n]
    
    # Sets A and B (using sets for O(1) lookups)
    set_a = set(input_data[2+n : 2+n+m])
    set_b = set(input_data[2+n+m : 2+n+2*m])
    
    # Calculate total happiness using generator expression with sum
    happiness = sum((1 if x in set_a else -1 if x in set_b else 0) for x in arr)
    
    print(happiness)

if __name__ == '__main__':
    solve()
