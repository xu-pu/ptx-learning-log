#!/usr/bin/env python

import sys

line = sys.stdin.readline().split()[0]
pages = [int(num) for num in sorted(set(line.split(',')))]
record = []
start, end = 0, 0
continuous = False
for index in range(len(pages)):
    if index == 0:
        start = pages[index]
    elif pages[index] == pages[index-1] + 1:
        continuous = True
        end = pages[index]
    elif not continuous:
        record.append(str(start))
        start = pages[index]
        continuous = False
    else:
        record.append(str(start) + '-' + str(end))
        start = pages[index]
        continuous = False
if continuous:
    record.append(str(start) + '-' + str(end))
else:
    record.append(str(start))
print ','.join(record)
