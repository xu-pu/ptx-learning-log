#!/usr/bin/env python

import sys

n, start, target = [int(num) for num in sys.stdin.readline().split()]
permutation =  [int(num) for num in sys.stdin.readline().split()]
result = 0
next_position = start
while(next_position != target):
    next_position = permutation[next_position-1]
    result += 1
    if next_position == start:
        result = -1
        break
print result
