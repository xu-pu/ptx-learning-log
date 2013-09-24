#!/usr/bin/env python
# Codeforce 186A

import sys

first, second = [s.split()[0] for s in sys.stdin.readlines()]
result = "NO"
if len(first) == len(second):
    diff = 0
    diff_list = []
    for char in range(len(first)):
        if first[char] != second[char]:
            diff = diff + 1
            diff_list.append([first[char], second[char]])
            if diff > 2:
                break
    if diff == 0:
        result = "YES"
    elif diff == 2:
        if diff_list[0][0] == diff_list[1][1] and diff_list[0][1] == diff_list[1][0]:
            result = "YES"

print result
