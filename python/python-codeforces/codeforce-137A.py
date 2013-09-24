#!/usr/bin/env python

import sys

class Hand(object):
    def __init__(self):
        self.count = 0
        self.amount = 0
        self.type = None
    
    def take(self, o):
        if self.amount == 5:
            # when hand full
            self.count += 1
            self.amount = 1
            self.type = o
        elif self.type == o:
            # hand not full and same type
            self.amount += 1
        elif self.type == None:
            # first time
            self.type = o
            self.amount = 1
        else:
            # different type
            self.count += 1
            self.type = o
            self.amount = 1

    def empty(self):
        self.count += 1
        self.amount = 0
        self.type = None

l = sys.stdin.readline().split()[0]
hand = Hand()
for o in l:
    hand.take(o)
hand.empty()
print hand.count
