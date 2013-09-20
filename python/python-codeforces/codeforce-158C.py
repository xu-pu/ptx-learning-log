#!/usr/bin/env python

import sys

class Interpreter(object):
    def __init__(self):
        self.cwd = []
    
    def pwd(self):
        if len(self.cwd) == 0:
            print '/'
        else:
            print '/' + '/'.join(self.cwd) + '/'

    def cd(self, path):
        if path[0] == '/':
            self.cwd = []
        for segment in path.split('/'):
            if segment == '..' and len(self.cwd) > 0:
                self.cwd.pop()
            elif segment == '':
                pass
            else:
                self.cwd.append(segment)

n = int(sys.stdin.readline())
commands = [sys.stdin.readline().split() for line in range(n)]
inter = Interpreter()
for command in commands:
    if command[0] == 'pwd':
        inter.pwd()
    elif command[0] == 'cd':
        inter.cd(command[1])
