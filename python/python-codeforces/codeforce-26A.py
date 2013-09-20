#!/usr/bin/env python
# Codeforce 26A

import sys
n = int(sys.stdin.readline())

# handle prime number generation
prime_list = [2,3,5,7,11,13,17,19,23]
def get_prime(n):
    if n > len(prime_list)-1:
        new_prime = prime_list[-1] + 1
        found = False
        while not found:
            found = True
            for prime in prime_list:
                if new_prime % prime == 0:
                    found = False
                    new_prime = new_prime + 1
                    break
        prime_list.append(new_prime)
        return new_prime
    else:
        return prime_list[n]

def valid(n):
    factor_counter = 0
    factor_list = []
    prime_cursor = 0
    next_prime = get_prime(prime_cursor)

    while next_prime <= n:
        if n % next_prime == 0:
            factor_list.append(next_prime)
            n = n / next_prime
            factor_counter = factor_counter + 1
            if factor_counter > 2:
                break
        prime_cursor = prime_cursor + 1
        next_prime = get_prime(prime_cursor)

    if factor_counter == 2:
        return True
    else:
        return False
    
count = 0
for number in range(6,n+1):
    if valid(number):
        count = count + 1
print count
