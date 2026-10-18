# Problem 18 -Set Mutations
# https://www.hackerrank.com/challenges/py-set-mutations/problem


n = int(input())
s = set(map(int, input().split()))

for _ in range(int(input())):
    operation, length = input().split()
    other_set = set(map(int, input().split()))

    if operation == "intersection_update":
        s.intersection_update(other_set)
    elif operation == "update":
        s.update(other_set)
    elif operation == "symmetric_difference_update":
        s.symmetric_difference_update(other_set)
    elif operation == "difference_update":
        s.difference_update(other_set)

print(sum(s))
