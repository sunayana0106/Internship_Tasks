# Problem 6- Introduction to Sets
# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):
    # your code goes here
    distinct_heights = set(array)
    return sum(distinct_heights) / len(distinct_heights)
