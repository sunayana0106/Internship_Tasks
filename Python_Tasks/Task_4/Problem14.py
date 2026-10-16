# Problem 14 - Set .add()
# https://www.hackerrank.com/challenges/py-set-add/problem

n = int(input())
stamps = set()

for _ in range(n):
    stamps.add(input().strip())

print(len(stamps))
