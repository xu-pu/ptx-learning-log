#!/usr/bin/env python
# Codeforce 278B

import sys, string

class Cursor:

    def __init__(self, length):
        self.cursor = [0] * length
        self.length = length

    def increase(self):
        if self.cursor[-1] == 25:
            count = 1
            while count < self.length:
                if self.cursor[-(count+1)] == 25:
                    count = count+1
                else:
                    break
            if count == self.length:
                return True
            else:
                self.cursor[-(count+1)] = self.cursor[-(count+1)] + 1
                while count > 0:
                    self.cursor[-count] = 0
                    count = count-1
                return False
        else:
            self.cursor[-1] = self.cursor[-1] + 1
            return False


l = sys.stdin.readlines()
n = int(l[0])
titles = [line.split()[0] for line in l[1:]]
alphabet = string.lowercase
length = 1
sub_string = ""

found = False
while not found:
    c = Cursor(length);
    cursor_limit = False
    # if found, terminate
    while not cursor_limit and not found:
        sub_string = "".join([alphabet[offset] for offset in c.cursor])
        # found is all cases passed
        found = True 
        for title in titles:
            if title.find(sub_string) != -1:
                found = False
                break
        cursor_limit = c.increase()
    length = length + 1

print sub_string
