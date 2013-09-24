#!/usr/bin/env python

import sys
line = sys.stdin.readline().split()[0]
words = line.split('WUB')
s = ' '.join([word for word in words if word != ''])
print s
