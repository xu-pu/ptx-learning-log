#!/usr/bin/env python

import sys

n = int(sys.stdin.readline())
matrix = [[int(num) for num in line.split()] for line in sys.stdin.readlines()]
row_sum = [sum(row) for row in matrix]
column_sum = [sum([row[column] for row in matrix]) for column in range(n)]
counter = 0
for row in range(n):
    for column in range(n):
        if row_sum[row] < column_sum[column]:
            counter += 1
print counter
