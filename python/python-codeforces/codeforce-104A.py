#!/usr/bin/env python
# Codeforce 104A

import sys
n = int(sys.stdin.readline())
need = n-10
if need < 1 or need > 11:
    chance = 0
elif need == 10:
    chance = 15
else:
    chance = 4
print chance
