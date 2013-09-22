#!/usr/bin/env python
# Codeforce 227A

import sys

def region_test(x,y):
    if x > 0 and y >= 0:
        return 1
    elif x <= 0 and y > 0:
        return 2
    elif x < 0 and y <= 0:
        return 3
    elif x >= 0 and y < 0:
        return 4


points = [[int(num) for num in line.split()] for line in sys.stdin.readlines()]

ABx, ABy, BCx, BCy = [ points[1][0] - points[0][0],
                       points[1][1] - points[0][1],
                       points[2][0] - points[1][0],
                       points[2][1] - points[1][1]]

AB = region_test(ABx,ABy)
BC = region_test(BCx,BCy)

if BC%4 == (AB-1)%4:
    result = 'RIGHT'
elif BC == AB:
    result = 'TOWARDS'
elif BC%4 == (AB+1)%4:
    result = 'LEFT'
print result
