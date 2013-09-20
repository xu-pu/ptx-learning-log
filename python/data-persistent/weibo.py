#!/usr/bin/env python
# -*- utf-8 -*-

import sqlite3 as sqlite
import sys, os
import requests, json

#----------------------------------------------------------------------------------
# persistent related constants
#----------------------------------------------------------------------------------

data_dir       = os.environ['HOME'] + '/Dropbox/code/random-tests/sqlite'
sql_db_path    = data_dir + '/sql-test.db'
orm_db_path    = data_dir + '/orm-test.db'

json_following = data_dir + '/following.json'
json_follower  = data_dir + '/follower.json'

#----------------------------------------------------------------------------------
# OAuth and API related constants
#----------------------------------------------------------------------------------

api_follower   = 'https://api.weibo.com/2/friendships/followers.json'
api_following  = 'https://api.weibo.com/2/friendships/friends.json'
api_myfeed     = 'https://api.weibo.com/2/statuses/user_timeline.json'
api_feed       = ''

token = '2.003WDnhCEfNZFDc811f9ffa9TP9iwB'
uid = '2479339722'

#----------------------------------------------------------------------------------
# Directly fetch with internet access
#----------------------------------------------------------------------------------

def get_followers():
    resp = requests.get(api_follower, 
                        params={'access_token': token, 'uid': uid, 'count': 200})
    result = resp.json()
    follower_list = result['users']
    while (result['next_cursor'] != 0):
        param = {'access_token': token, 
                 'uid': uid, 
                 'count': 200, 
                 'cursor': result['next_cursor']}
        resp = requests.get(api_follower, params=param)
        result = resp.json()
        follower_list += result['users']
    return follower_list

def get_followings(token, uid):
    resp = requests.get(api_following, 
                        params={'access_token': token, 'uid': uid, 'count': 200})
    result = resp.json()
    following_list = result['users']
    while (result['next_cursor'] != 0):
        param = {'access_token': token, 
                 'uid': uid, 
                 'count': 200, 
                 'cursor': result['next_cursor']}
        resp = requests.get(api_following, params=param)
        result = resp.json()
        follower_list += result['users']
    return following_list

def get_newsfeed():
    pass


#----------------------------------------------------------------------------------
# Use JSON as temp file
#----------------------------------------------------------------------------------

def write_follower(follower_list):
    with open(json_follower, 'a') as f:
        f.write(json.dumps(follower_list))

def load_follower():
    with open(json_follower, 'r') as f:
        return json.loads(f.read())

def write_following(following_list):
    with open(json_following, 'a') as f:
        f.write(json.dumps(following_list))

def load_following():
    with open(json_following, 'r') as f:
        return json.loads(f.read())

#----------------------------------------------------------------------------------
# Database persistent using SQL
#----------------------------------------------------------------------------------

insert_account  = 'INSERT OR REPLACE INTO Account VALUES (?,?,?,?)'
insert_follower = 'INSERT INTO Follower VALUES (?)'
insert_following = 'INSERT INTO Following VALUES (?)'

create_account = '''
CREATE TABLE IF NOT EXISTS Account (
  id INTEGER PRIMARY KEY,
  screen_name TEXT,
  display_name TEXT,
  gender TEXT );
'''

recreate_follower = '''
DROP TABLE IF EXISTS Follower;
CREATE TABLE Follower (
  id INTEGER PRIMARY KEY,
  FOREIGN KEY (id) REFERENCES Account(id) );
'''

recreate_following = '''
DROP TABLE IF EXISTS Following;
CREATE TABLE Following (
  id INTEGER PRIMARY KEY,
  FOREIGN KEY (id) REFERENCES Account(id) );
'''

def sql_update_follower(follower_list):
    con = sqlite.connect(sql_db_path)
    with con:
        cur = con.cursor()
        cur.executescript(create_account)
        cur.executescript(recreate_follower)
        for p in follower_list:
            cur.execute(insert_account,  
                        (p['id'], p['screen_name'], p['name'], p['gender']))
            cur.execute(insert_follower, (p['id'],))

def sql_update_following(following_list):
    con = sqlite.connect(sql_db_path)
    with con:
        cur = con.cursor()
        cur.executescript(create_account)
        cur.executescript(recreate_following)
        for p in following_list:
            cur.execute(insert_account,  
                        (p['id'], p['screen_name'], p['name'], p['gender']))
            cur.execute(insert_following, (p['id'],))

def sql_add_content(cid):
    pass

def sql_update_content(cid):
    con = sqlite.connect(sql_db_path)
    with con:
        cur = con.cursor()
        cur.executescript()
    pass

#----------------------------------------------------------------------------------
# Database persistent using ORM
#----------------------------------------------------------------------------------


#----------------------------------------------------------------------------------
# Execute
#----------------------------------------------------------------------------------

if __name__ == '__main__':
    sql_follower(load_follower())
    sql_following(load_following())
