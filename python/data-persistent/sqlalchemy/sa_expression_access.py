#!/usr/bin/env python

import json
from sqlalchemy import create_engine

from sa_expression_def import users, tweets, metadata
from weibo_test import test_account, get_all_timeline

engine = create_engine('sqlite:///:memory')

# Create Database

metadata.create_all(engine)

conn = engine.connect()

for tweet in get_all_timeline(test_account):
    uid = tweet['user']['id']
    tid = tweet['id']
    if conn.execute(tweets.select(tweets.c.id == tid)).fetchone():
        break
    if not conn.execute(users.select(users.c.id == uid)).fetchone():
        conn.execute(users.insert().values(id=uid, profile=json.dumps(tweet['user'])))
    conn.execute(tweets.insert().values(id=tid, user_id=uid, content=json.dumps(tweet)))
