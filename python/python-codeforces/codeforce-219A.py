#!/usr/bin/env python

import sys

n = int(sys.stdin.readline())
line = sys.stdin.readline().split()[0]

# parse the string
record = {}
for char in line:
    if char in record:
        record[char] += 1
    else:
        record[char] = 1

# check
exist = True
result = ''
for char in record:
    if record[char] % n == 0:
        result = result + char * (record[char]/n)
    else:
        exist = False
        break
if exist:
    print result * n
else:
    print -1
