#!/usr/bin/env python
#===========================================================================
#
# HELLO REDIS !
#
# This is the hello world program of me learning Redis over Arch Linux
#
#===========================================================================

import redis

def hello_world(connection):
    connection.set('key', 'value') # store key-value pair 
    my_value = connection.get('key') # get value by key
    connection.delete('key') # delete pair
    
    print(my_value)


def hello_integer(connection):
    connection.set('hello_integer', 1)
    connection.incr('hello_integer')
    connection.decr('hello_integer')
    int_str = connection.get('hello_integer') # return integer_string

    print(int_str)


def hello_list(connection):

    # push item
    for item in ['item_1', 'item_2', 'item_3']:
        connection.rpush('hello_list', item)

    # pop item
    item_pop = connection.rpop('hello_list')

    # query item
    my_list = connection.lrange('hello_list', 0, -1) # from head to tail
    my_list_len = connection.llen('hello_list')
    item_x = connection.lindex('hello_list', 1)

    print(my_list)
    print(my_list_len)
    print(item_x)
    print(item_pop)


def hello_set(connection):

    # push items
    for item in ['item_1', 'item_2', 'item_3']:
        connection.sadd('hello_set', item)

    # query
    my_set = connection.smembers('hello_set')
    my_set_len = connection.scard('hello_set')

    print(my_set)
    print(my_set_len)


def hello_ordered_set(connection):

    # push items
    connection.zadd('hello_ordered', 'item_1', 30) # value with z-index (score)
    connection.zadd('hello_ordered', 'item_2', 20) 
    connection.zadd('hello_ordered', 'item_3', 50)

    connection.zincrby('hello_ordered', 'item_1', 2) # z increment

    # query
    my_ordered_score = connection.zrange('hello_ordered', 0, -1, withscores=True)
    my_ordered = connection.zrange('hello_ordered', 0, -1, withscores=False) # list without z-index
    my_ordered_score.reverse()
    my_ordered.reverse()

    print(my_ordered_score)
    print(my_ordered)


if __name__ == '__main__':
    r_server = redis.Redis('localhost') # set up connection to the redis server
    hello_world(r_server)
    hello_integer(r_server)
    hello_list(r_server)
    hello_set(r_server)
    hello_ordered_set(r_server)
