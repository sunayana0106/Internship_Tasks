# Problem 1- Find the Runner-Up Score!
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

    n = int(input())
    arr = map(int, input().split())
    scores = sorted(list(set(arr)))
    
    print(scores[-2])
