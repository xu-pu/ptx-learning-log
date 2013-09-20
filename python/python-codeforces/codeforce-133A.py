#!/usr/bin/env python
# Codeforce problem 133A

import sys

text = sys.stdin.readline().split()[0]
valid = ['H', 'Q', '9']
result = 'NO'
for char in text:
    for ins in valid:
        if char == ins:
            result = 'YES'
            break
print(result)
