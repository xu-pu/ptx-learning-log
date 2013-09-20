#!/usr/bin/env python

import sys

line = sys.stdin.readline().split()[0]
length = len(line)
count = 0
for start in range(length-1):
    for end in range(start+1,length):
        head, tail, match = start, end, 0
        while(line[head] == line[tail] and head < tail):
            match += 1
            head += 1
            tail -= 1
        count += match
print count
            
