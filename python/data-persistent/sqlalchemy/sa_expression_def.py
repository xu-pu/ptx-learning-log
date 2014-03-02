#!/usr/bin/env python

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

#==================================
# Define Database with Metadata
#==================================

metadata = MetaData()

tweets = Table( 'tweets', metadata,
                Column('id', Integer, primary_key=True),
                Column('user_id', None, ForeignKey('users.id')),
                Column('content', String, nullable=False))

users = Table( 'users', metadata,
                Column('id', Integer, primary_key=True),
                Column('profile', String, nullable=False))

assert users.metadata is metadata
assert tweets.metadata is metadata

if __name__ == '__main__':
    pass
