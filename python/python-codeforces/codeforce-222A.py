#!/usr/bin/env python

import sys

n, k = [int(num) for num in sys.stdin.readline().split()]
line = [int(num) for num in sys.stdin.readline().split()]
k = k-1
tail, head = list(set(line[k:])), line[:k]
if len(tail) == 1:
    result = len(head)
    for char in head[::-1]:
        if char == tail[0]:
            result -= 1
        else:
            break
else:
    result = -1
print result
