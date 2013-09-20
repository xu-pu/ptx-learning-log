#!/usr/bin/env python
# Codeforce problem 131A

import sys

def is_caps(l):
    for char in l[1:]:
        if char.islower():
            return False
    return True

def inverse(c):
    if c.isupper():
        return c.lower()
    else:
        return c.upper()

text = sys.stdin.readline().split()[0]
if is_caps(text):
    text = inverse(text[0]) + text[1:].lower()
print(text)
