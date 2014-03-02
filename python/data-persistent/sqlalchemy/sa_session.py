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

session.add_all([
    User(),
    User(),
    User(),
])

session.dirty
session.new
session.commit()
session.rollback()

for instance in session.query(User).order_by(User.id):
    pass

for name, fullname in session.query(User.name, User.fullname):
    pass

for instance in session.query(User.name('name_label')).order_by(User.id):
    pass
