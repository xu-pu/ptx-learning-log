#!/usr/bin/env python

import sys

n = int(sys.stdin.readline())
stat = [sys.stdin.readline().split()[0] for line in range(n)]
result = 0
for line in stat:
    if line == 'X++' or line == '++X':
        result += 1
    else:
        result -= 1
print result
