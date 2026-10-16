# Problem 16- Collections.Counter()
# https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

num_shoes = int(input())
shoe_inventory = Counter(map(int, input().split()))
num_customers = int(input())

total_earned = 0

for _ in range(num_customers):
    size, price = map(int, input().split())
    if shoe_inventory[size] > 0:
        total_earned += price
        shoe_inventory[size] -= 1

print(total_earned)
