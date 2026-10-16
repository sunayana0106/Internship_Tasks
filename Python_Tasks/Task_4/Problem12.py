# Problem 12 -Introduction to Sets
# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):
    distinct_heights = set(array)
    return round(sum(distinct_heights) / len(distinct_heights), 3)
