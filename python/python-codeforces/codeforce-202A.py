#!/usr/bin/env python

import sys

line = list(sys.stdin.readline().split()[0])
line.sort(reverse=True)
print ''.join([char for char in line if char == line[0]])

