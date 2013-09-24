#!/usr/bin/env python

import sys

n = int(sys.stdin.readline())
digits = [num for num in sys.stdin.readline().split()]
digit_set = set(digits)
digit_set.add('.')

ip_addresses, numbers, number_dict = [], [], {1: [], 2: [], 3: []}

# find all posible numbers
# 1 digit
for d in digits:
    number_dict[1].append(d)

# 2 digits
for first in digits:
    for second in digits:
        if first != '0':
            number_dict[2].append(first+second)

# 3 digits
for first in digits:
    for second in digits:
        for third in digits:
            num = first + second + third
            if first != '0' and int(num) <= 255:
                number_dict[3].append(num)

numbers = number_dict[1] + number_dict[2] + number_dict[3]


# scan all posible ip addresses consists of posible numbers

# symetric, 1=4, 2=3
for first in numbers:
    for second in numbers:
        ip = '.'.join([first,second,second[::-1],first[::-1]])
        if set(ip) == digit_set:
            ip_addresses.append(ip)


# half symetirc, 1=4, 2!=3

def search23(len2, len3):
    for first in numbers:
        for second in number_dict[len2]:
            for third in number_dict[len3]:
                ip = '.'.join([first,second,third,first[::-1]])
                if set(ip) == digit_set:
                    s  = list(second + third)
                    sr = list(s)
                    sr.reverse()
                    if s == sr:
                        ip_addresses.append(ip)
                
for second in [1,2,3]:
    for third in [1,2,3]:
        if second != third:
            search23(second,third)

# asymetric, 1!=4

def search14(len1, len4):
    for first in number_dict[len1]:
        for second in numbers:
            for third in numbers:
                for fourth in number_dict[len4]:
                    ip = '.'.join([first,second,third,fourth])
                    if set(ip) == digit_set:
                        s  = list(first + second + third + fourth)
                        sr = list(s)
                        sr.reverse()
                        if s == sr:
                            ip_addresses.append(ip)

for first in [1,2,3]:
    for fourth in [1,2,3]:
        if first != fourth:
            search14(first,fourth)


# print
print len(ip_addresses)
for line in ip_addresses:
    print line
