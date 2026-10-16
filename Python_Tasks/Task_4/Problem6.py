# Problem 6- Find the Runner-Up Score!
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    sorted_scores = sorted(list(set(arr)))
    print(sorted_scores[-2])
