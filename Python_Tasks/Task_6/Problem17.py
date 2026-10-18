# Problem 17 - Check Strict Superset
# https://www.hackerrank.com/challenges/py-check-strict-superset/problem

a = set(map(int, input().split()))
n = int(input())

# Check if a is a strict superset of all other n sets
result = all(a.issuperset(set(map(int, input().split()))) for _ in range(n))

print(result)
