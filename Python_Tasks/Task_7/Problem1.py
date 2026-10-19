# Problem 1- Set .symmetric_difference() Operation
# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

n = int(input())
set_english = set(map(int, input().split()))

m = int(input())
set_french = set(map(int, input().split()))

print(len(set_english.symmetric_difference(set_french)))
