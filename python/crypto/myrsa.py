#!/bin/env python

import random

def gen_m_n():
    m_index = n_index = random.randint(20, 100)
    while m_index == n_index:
        n_index = random.randint(20, 100)
    return get_prime(m_index), get_prime(n_index)

def gen_private_key(m, n):
    pk = { 'n': m*n }
    phi = (m-1)*(n-1)
    return pk

def gen_public_key(m, n, pk):
    pub_key = { 'n': m*n }
    phi = (m-1)*(n-1)
    for n in range(phi):
        if n * pk['e'] % phi == 1:
            pub_key['d'] = n
            return pub_key

def encrypt_number(pub_key, msg):
    return cipher ** pub_key['d'] % pub_key['n']

def decrypt_number(pk, cipher):
    return cipher ** pk['d'] % pk['n']

def demo(msg):
    m, n = gen_m_n()
    pk = gen_private_key(m, n)
    pub = gen_public_key(m, n, pk)
    cipher = encrypt_number(pub, msg)
    original = decrypt_number(pk, cipher)

if __name__ == '__main__':
    demo(65)
