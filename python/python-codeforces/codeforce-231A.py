#!/usr/bin/env python
# Codeforce problem 231A

import sys

input_list = sys.stdin.readlines()
n = int(input_list[0])

count = 0
for i in range(1,n+1):
    first, second, third = [int(item) for item in input_list[i].split()]
    if first + second + third >= 2:
        count = count + 1

print(count)
