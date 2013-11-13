#!/bin/env python

from tasks import add
from time import sleep

def hello_celery():
    result = add.delay(4,4)
    if result.ready():
        print(result.result)
    else:
        print('not ready yet')

    wait_time = 0
    while not result.ready():
        sleep(0.1)
        wait_time += 0.1
    print('result is ' + str(result.result))
    print('waited %d seconds' % wait_time)

if __name__ == '__main__':
    hello_celery()
