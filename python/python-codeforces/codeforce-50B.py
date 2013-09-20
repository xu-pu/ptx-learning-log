#!/usr/bin/env python

import sys

line = sys.stdin.readline().split()[0]

record = {}
for char in line:
    if char in record:
        record[char] += 1
    else:
        record[char] = 1

result = 0
for entry in record:
    result += record[entry] ** 2

print result
