#!/usr/bin/env python
# -*- utf-8 -*-
#======================================================================

import os, re

#======================================================================

DIR_NAME   = os.path.dirname(__file__)
UTF_SAMPLE = os.path.join(DIR_NAME, 'city-data-1.txt')

#======================================================================

def substring_operations():
    my_str = 'somestring'
    char = my_str[0]
    char = my_str[-1]
    sub_str = my_str[1:3]

def str_pattern():    
    S.find('pa')
    S.replace('pa', "XYZ")
    line = 'aaa,bbb,cccc,dd'
    line.split(',')

def utf8_str():
    record = {}
    with open(UTF_SAMPLE, 'r') as f:
        for line in f.readlines():
            region, city, latitude, longitude = line.split()
            latitude  = float((re.search('^北纬(?P<latitude>.*)$' , latitude )).group('latitude'))
            longitude = float((re.search('^东经(?P<longitude>.*)$', longitude)).group('longitude'))
            if region not in record:
                record[region] = []
            record[region].append((city, latitude, longitude))
    for region in record:
        print(region)
        print(record[region])

if __name__ == '__main__':
    utf8_str()
