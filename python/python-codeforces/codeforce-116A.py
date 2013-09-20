#!/usr/bin/env python
# Codeforce problem 116A

import sys

input_list = sys.stdin.readlines()
count = int(input_list[0])

max_count = 0
num_count = 0
for i in range(1,count):
    record = input_list[i].split()
    getout = int(record[0])
    getin = int(record[1])
    num_count = num_count - getout
    num_count = num_count + getin
    if num_count > max_count:
        max_count = num_count
print(max_count)
