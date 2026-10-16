# Problem 13 -Symmetric Difference
# https://www.hackerrank.com/challenges/symmetric-difference/problem

m = int(input())
set_a = set(map(int, input().split()))
n = int(input())
set_b = set(map(int, input().split()))
sym_diff = set_a.symmetric_difference(set_b)
for num in sorted(sym_diff):
    print(num)
