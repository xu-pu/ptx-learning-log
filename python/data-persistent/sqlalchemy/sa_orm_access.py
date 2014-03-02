#!/usr/bin/env python

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from hello_sa_orm import User
from hello_sa_expression import users, addresses, metadata

#=========================

engine = create_engine('sqlite:///:memory', echo=True) # connection

Session = sessionmaker(bind=engine)
# Session = sessionmaker()
# Session.configure(bind=engine)

#=========================
# Access Database by ORM
#=========================

session = Session()
some_user = User()
session.add(some_user)
our_user = session.query(User).filter_by(name='ed').first()
# assert users.bind is engine

