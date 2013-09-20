#!/usr/bin/env python

import sys, itertools

def common_divisor(big, small):
    step, divisors = 1, []
    while(step <= small):
        if small % step == 0 and big % step == 0:
            divisors.append(step)
        step += 1
    return divisors

def match(length, s):
    for offset in range(length):
        for substring in range(0,len(s),length):
            if s[substring+offset] != s[offset]:
                return False
    return True


def obvious_false(slong, sshort):
    for cursor in range(len(sshort)):
        if slong[cursor] != sshort[cursor]:
            return True
    return False

s1 = sys.stdin.readline().split()[0]
s2 = sys.stdin.readline().split()[0]
if len(s1) >= len(s2):
    sshort, slong = s2, s1
else:
    sshort, slong = s1, s2

result = 0
if obvious_false(slong, sshort):
    pass
else:
    divisors = common_divisor(len(slong), len(sshort))
    for length in divisors:
        if match(length, slong):
            for scalar in itertools.count(1):
                multiple = length * scalar
                if len(divisors) == 0 or multiple > divisors[-1]:
                    break
                elif multiple in divisors:
                    result += 1
                    divisors.remove(multiple)
print result
