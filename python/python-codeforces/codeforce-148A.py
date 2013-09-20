#!/usr/bin/env python
# Codeforce problem 82A

import sys

def excluded(num,l):
    for factor in l:
        if num % factor == 0:
            return False
    return True

param = [int(item) for item in sys.stdin.readlines()]
n = param[4]
factors = param[:4]
for num in range(1, n+1):
    if excluded(num,factors):
        n = n - 1
print(n)
