#!/usr/bin/env python

import sys

n = int(sys.stdin.readline())
l = [int(num) for num in sys.stdin.readline().split()]

odd  = filter(lambda x: x % 2 == 1, l)
even = filter(lambda x: x % 2 == 0, l)

if len(odd) == 1:
    print l.index(odd[0])+1
else:
    print l.index(even[0])+1
