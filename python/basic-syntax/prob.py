#!/usr/bin/env python

def probability(n):
    return 100 * (1 - 0.99 ** n)

if __name__ == '__main__':
    l = (100,200,500,800,1000)
    for times in l:
        print 'when try %d times, probability of winning is %f' \
            % (times, probability(times))
