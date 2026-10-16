# Problem 4- Find a String
# https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(string, sub_string):
   count = 0
   start = 0
   while True:
        idx = string.find(sub_string, start)
        if idx == -1:
            break
        count += 1
        start = idx + 1  # Move past the current match to catch overlaps
        
   return count
