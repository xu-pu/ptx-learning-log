#!/usr/bin/env python

import sys

paint = [list(line.split()[0]) for line in sys.stdin.readlines()]
result = False
for line in range(4):
    for cursor in range(3):
        if paint[line][cursor] == paint[line][cursor+1]:
            record, char = [], paint[line][cursor]
            if line != 0:
                record += paint[line-1][cursor:cursor+2]                
            if line != 3:
                record += paint[line+1][cursor:cursor+2]
            if char in record:
                result = True
                break
    if result:
        break

if result:
    print 'YES'
else:
    print 'No'
