#!/usr/bin/env python
# Codeforce problem 82A

import sys

first, second = [line.split()[0].lower() for line in sys.stdin.readlines()]
if first == second:
    result = 0
elif first > second:
    result = 1
else:
    result = -1
print(result)
