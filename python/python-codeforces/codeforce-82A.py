#!/usr/bin/env python
# Codeforce problem 82A

import sys

def count(num):
    bound = 5
    step = 1
    result = -1
    while num > bound:
        bound = bound * 2 + 5
        step = step * 2
    if num == bound:
        pass
    else:
        result = ( num - bound + step * 5 - 1 ) / step
    return result

name = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
n = int(sys.stdin.readline())
print(name[count(n)])
