#!/usr/bin/env python

import sys, itertools

a, b = [bin(int(num)) for num in sys.stdin.readline().split()]
template = []
if len(a) > len(b):
    slong, sshort = a[2:], b[2:]
else:
    slong, sshort = b[2:], a[2:]
len_long, len_short = len(slong), len(sshort)

for position in range()
