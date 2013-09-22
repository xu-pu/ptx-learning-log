#!/usr/bin/env python
# Codeforce 58B

import sys
n = int(sys.stdin.readline())

def find_max_coin(num, begin):
    while begin <= num:
        if num % begin == 0:
            return begin
        begin = begin + 1

coin_list = [n]
iter_factor = 2
iter_coin = n
while iter_coin != 1:
    iter_factor = find_max_coin(iter_coin, iter_factor)
    iter_coin = iter_coin / iter_factor
    coin_list.append(iter_coin)
print " ".join([str(coin) for coin in coin_list])
