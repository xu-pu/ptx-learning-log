#!/usr/bin/env python

import sys

name, address, text = [line.split()[0] for line in sys.stdin.readlines()]
ideal = list(name + address)
ideal.sort()
remain = list(text)
remain.sort()
if ideal == remain:
    print 'YES'
else:
    print 'NO'
