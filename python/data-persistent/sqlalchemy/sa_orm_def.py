#!/usr/bin/env python

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Sequence
from sqlalchemy.ext.declarative import declarative_base

#=========================
# Bind with ORM
#=========================

Base = declarative_base()    

class Profile(Base):
    __table__ = 'profiles'
    
    id = Column(Integer, primary_key=True)
    profile = Column(String)

    def __init__(self, id, profile):
        self.id = id
        self.profile = profile
    
    def _repr__(self):
        return 'uid: ' + str(self.id)


class Tweet(Base):
    __table__ = 'tweets'
    
    id = Column(Integer, primary_key=True)
    user = Column(ForeignKey('profiles.id'))
    content = Column(String)

    def __init__(self, id, user, content):
        self.id = id
        self.user = user
        self.content = content
    
    def _repr__(self):
        return 'tweet: ' + str(self.id)


class Account(Base):
    __table__ = 'accounts'
    
    id = Column(Integer, primary_key=True)
    profile = Column(ForeignKey('profiles.id'))
    token = Column(String)

    def __init__(self, id, user, content):
        self.id = id
        self.user = user
        self.content = content

    def fetch_home_timeline(self):
        pass

    def fetch_my_timeline(self):
        pass
    
    def fetch_my_archive(self):
        pass

    def fetch_my_follower(self):
        pass

    def fetch_my_following(self):
        pass

    def _repr__(self):
        return 'tweet: ' + str(self.id)
