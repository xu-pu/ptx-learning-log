#!/usr/bin/env python

import sys, re

s = sys.stdin.readline().split()[0]
pattern = '.*(0000000|1111111).*'
match = re.match(pattern, s)
if match:
    print 'YES'
else:
    print 'NO'
