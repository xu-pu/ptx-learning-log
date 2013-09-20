#!/usr/bin/env python
# Codeforce 266A

import sys
n, l = sys.stdin.readlines()
n = int(n)
iter = 0
count = 0
while iter < n-1:
    if l[iter] == l[iter+1]:
        count = count + 1
    iter = iter + 1
print count
