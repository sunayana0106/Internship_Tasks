# Problem 14 - Set .intersection() Operation
# https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

n = int(input())
set_a = set(map(int, input().split()))
m = int(input())
set_b = set(map(int, input().split()))

print(len(set_a.intersection(set_b)))
