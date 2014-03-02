#!/usr/bin/env python

import requests

# Weibo Authentication Information

client_key    = '1021664904'
client_secret = ''
api_key       = ''
access_scope  = ''
redirect_uri  = ''

token_example = '2.003WDnhCMinIHBe21908739b03Wejh'
uid_example   = '2479339722'

API_BASE = 'https://api.weibo.com/2'
API_TIMELINE  = '/statuses/home_timeline.json'


class WeiboAccount(object):
    def __init__(self, uid, token=None):
        self.uid = uid
        self.access_token = token
        self.user_info = { 'access_token': self.access_token }

    def call_api(self, api, query):
        query['access_token'] = self.access_token
        query['uid'] = self.uid
        resp = requests.get(API_BASE+api, params=query)
        return resp.json()

def get_all_timeline(acocunt):
    in_progress = True
    query = {'count': 100}
    while (in_progress):
        result = acocunt.call_api(API_TIMELINE, query)
        for feed in result['statuses']:
            yield feed
        query['max_id'] = result['next_cursor']
        in_progress = result['next_cursor'] != 0


test_account = WeiboAccount(uid_example, token=token_example)

def my_test():
    for tweet in get_all_timeline(test_account):
        print(tweet['created_at'])

if __name__ == '__main__':
    pass
