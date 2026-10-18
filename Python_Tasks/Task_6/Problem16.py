# Problem 16- Check Subset
# https://www.hackerrank.com/challenges/py-check-subset/problem


for _ in range(int(input())):
    input()  # Number of elements in set A (not needed when using sets)
    a = set(map(int, input().split()))
    
    input()  # Number of elements in set B (not needed when using sets)
    b = set(map(int, input().split()))
    
    print(a.issubset(b))
