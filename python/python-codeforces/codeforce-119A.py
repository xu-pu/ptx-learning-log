#!/usr/bin/env python
# Codeforce problem 119A

import sys

def gcd(a,b):
    if a == 0 or b == 0:
        return a + b
    elif a > b:
        return gcd(a-b,b)
    elif a < b:
        return gcd(a,b-a)
    else:
        return a

first, second, heap = [int(item) for item in sys.stdin.readline().split()]

amount = gcd (first, heap)
first_turn = True
while heap >= amount:
    heap = heap - amount
    first_turn = not first_turn
    if first_turn:
        amount = gcd (first, heap)
    else:
        amount = gcd (second, heap)
if first_turn:
    print(1)
else:
    print(0)
