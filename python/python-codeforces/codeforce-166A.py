#!/usr/bin/env python

import sys

l = sys.stdin.readlines()
n, k = [int(num) for num in l[0].split()]
results = [[int(num) for num in line.split()] for line in l[1:]]

# in the following steps, nth-place means the index of it inside the array of sorted records
k = k-1

# amount of solved problems of kth-place
solve = [record[0] for record in results]
solve.sort()
solve.reverse()
ksolve = solve[k]
base = solve.index(ksolve)

# with same amount of solved problems
offset = k - base
time = [record[1] for record in results if record[0] == ksolve]
time.sort()
ktime = time[offset]
count = len([record for record in time if record == ktime]) 
print count
