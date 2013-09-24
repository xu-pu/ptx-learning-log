#!/usr/bin/env python

import sys

n = int(sys.stdin.readline())
inputs = [line.split()[0] for line in sys.stdin.readlines()]
full = lambda block: '0' * ( 4 - len(block)) + block

for line in inputs:
    if '::' in line:
        sections = line.split('::')
        if line == '::':
            # empty address
            template = ['0000'] * 8
        elif sections[0] == '':
            # zero in front
            blocks = sections[1].split(':')
            heading_zeros = ['0000'] * (8 - len(blocks)) 
            template =  heading_zeros + [full(block) for block in blocks]
        elif sections[1] == '':
            # zero in the back
            blocks = sections[0].split(':')
            tailing_zeros = ['0000'] * (8 - len(blocks))             
            template = [full(block) for block in blocks] + tailing_zeros
        else:
            # zero in the middle
            heading_blocks = sections[0].split(':')
            tailing_blocks = sections[1].split(':')
            zeros = ['0000'] * (8 - len(heading_blocks) - len(tailing_blocks))
            template = [full(block) for block in heading_blocks] + zeros + [full(block) for block in tailing_blocks]
    else:
        template = []
        for block in line.split(':'):
            template.append(full(block))
    print ':'.join(template)
