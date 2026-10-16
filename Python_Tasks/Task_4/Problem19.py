# Problem 19-Collections.Counter()
# https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

def solve():
    # Read number of shoes
    num_shoes = int(input())
    
    # Read list of shoe sizes and create a Counter object
    shoe_sizes = map(int, input().split())
    inventory = Counter(shoe_sizes)
    
    # Read number of customers
    num_customers = int(input())
    
    total_earned = 0
    
    # Process each customer's request
    for _ in range(num_customers):
        size, price = map(int, input().split())
        
        # Check if the shoe size is available in inventory
        if inventory[size] > 0:
            total_earned += price
            inventory[size] -= 1  # Decrease the count of that shoe size
            
    # Print the total money earned
    print(total_earned)

if __name__ == '__main__':
    solve()
