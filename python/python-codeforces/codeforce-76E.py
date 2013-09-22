#!/usr/bin/env python

import sys, itertools

n = int(sys.stdin.readline())
points = set([(int(line[0]), int(line[1])) for line in [sys.stdin.readline().split() for line in range(n)]])
acc = 0
for pair in itertools.combinations(points,2):
    acc += (pair[0][0]-pair[1][0])**2 + (pair[0][1]-pair[1][1])**2
print acc
