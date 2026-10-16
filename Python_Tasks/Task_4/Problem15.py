#Problem 15 - Word Order
#https://www.hackerrank.com/challenges/word-order/problem

from collections import OrderedDict
import sys
lines = sys.stdin.read().splitlines()
n = int(lines[0])
word_counts = OrderedDict()

for word in lines[1 : n + 1]:
  word_counts[word] = word_counts.get(word, 0) + 1
print(len(word_counts))
print(*(word_counts.values()))
