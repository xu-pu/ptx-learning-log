#!/usr/bin/env python
# Codeforce 242B

import sys
l = sys.stdin.readlines()
n = int(l[0])
points = [[int(num) for num in p.split()] for p in l[1:]]
minimum = min([p[0] for p in points])
maximum = max([p[1] for p in points])
result = -1
for i in range(n):
    if points[i] == [minimum, maximum]:
        result = i+1
        break
print result
