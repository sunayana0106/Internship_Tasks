# Problem 13-Nested Lists
# https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        
    grades = sorted(list(set([score for name, score in records])))
    second_lowest = grades[1]
    names = sorted([name for name, score in records if score == second_lowest])
    
    for name in names:
        print(name)
