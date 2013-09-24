#!/usr/bin/env python

import sys

n, t = [int(num) for num in sys.stdin.readline().split()]
line = list(sys.stdin.readline().split()[0])

for time in range(t): 
    for position in [boy for boy in range(n-1) if line[boy] == 'B' and line[boy+1] == 'G']:
        line[position], line[position+1] = 'G', 'B'

print ''.join(line)
