#!/usr/bin/env python

import sys

l = [line.split()[0] for line in sys.stdin.readlines()]
result = 'YES'
for line in l:
    if line != 'WBWBWBWB' and line != 'BWBWBWBW':
        result = 'NO'
        break
print result
