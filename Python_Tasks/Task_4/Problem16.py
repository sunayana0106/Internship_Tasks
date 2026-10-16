# Problem 16 -Nested Lists
# https://www.hackerrank.com/challenges/nested-list/problem

records = []  
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        
    unique_scores = sorted(list(set(score for name, score in records)))
    second_lowest = unique_scores[1]
    
    second_lowest_students = sorted([name for name, score in records if score == second_lowest])
    
    for name in second_lowest_students:
        print(name)
