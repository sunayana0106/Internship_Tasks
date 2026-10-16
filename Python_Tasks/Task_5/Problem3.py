# Problem 3- Mutations
# https://www.hackerrank.com/challenges/python-mutations/problem

def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    return ''.join(l)
