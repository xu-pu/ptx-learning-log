#!/usr/bin/env python

import sys, string

word = sys.stdin.readline().split()[0]
lower_counter = 0
for char in word:
    if char in string.lowercase:
        lower_counter += 1
upper_counter = len(word) - lower_counter
if lower_counter >= upper_counter:
    print word.lower()
else:
    print word.upper()
