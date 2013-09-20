#!/usr/bin/env python
# Codeforce 41A

import sys

l1, l2 = [s.split()[0] for s in sys.stdin.readlines()]
n1 = len(l1)
n2 = len(l2)
result = "YES"
if n1 != n2:
    result = "NO"
else:
    for i in range(n1):
        if l1[i] != l2[n1-i-1]:
            result = "NO"
            break
print result
