# Problem 12-Capitalize!
# https://www.hackerrank.com/challenges/capitalize/problem

def solve(s):
    return " ".join(word.capitalize() for word in s.split(" "))
