#!/usr/bin/env python

import sys, re

s = sys.stdin.readline().split()[0]
pattern  = '.*h.*e.*l.*l.*o.*'
match = re.match(pattern, s)
if match:
    print 'YES'
else:
    print 'NO'
