#!/usr/bin/env python

import sys, re, string

def number_to_string(num):
    if num >= 1 and num <= 26:
        return string.uppercase[num-1]
    elif num % 26 == 0:
        return number_to_string(num/26-1) + 'Z'
    else:
        return number_to_string(num/26) + string.uppercase[num%26-1]

def string_to_number(s):
    if len(s) == 1:
        return string.uppercase.index(s) + 1
    else:
        return 26 * string_to_number(s[:-1]) + string_to_number(s[-1])
    
pattern_rc = '^R(?P<row>[0-9]+)C(?P<column>[0-9]+)$'
pattern_alnum = '^(?P<column>[A-Z]+)(?P<row>[0-9]+)$'

n = int(sys.stdin.readline())
l = [line.split()[0] for line in sys.stdin.readlines()]

for line in l:
    match = re.match(pattern_rc, line)
    if match:
        # in RC form, convert to alnum form
        print number_to_string(int(match.group('column'))) + match.group('row')
    else:
        # in alnum form, convert to RC form
        match = re.match(pattern_alnum, line)
        print 'R' + match.group('row')  + 'C' + str(string_to_number(match.group('column')))
