# problem 7- String Split and Join
# https://www.hackerrank.com/challenges/python-string-split-and-join/problem

def split_and_join(line):
    # write your code here
    words=line.split(" ")
    new="-".join(words)
    return(new)
