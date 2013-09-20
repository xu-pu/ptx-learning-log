#!/usr/bin/env python

import sys, string

line = sys.stdin.readline().split()[0]
bad_string = sys.stdin.readline().split()[0]
bad_max = int(sys.stdin.readline())
bad_letters = [string.lowercase[position] for position in range(26) if bad_string[i] == '0'] 
bad_positions = [position for position in range(len(line)) if line[position] in bad_letters] 
record = []

for bad in range(bad_max+1):
    for region in line:
        for head in head_region:
            
            for tail in tail_region:
            
