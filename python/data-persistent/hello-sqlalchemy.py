#!/usr/bin/env python

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Sequence

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#=========================
# Connection to Database
#=========================

engine = create_engine('sqlite:///:memory', echo=True) # connection
Base = declarative_base()

Session = sessionmaker()
Session.configure(bind=engine)
# Session = sessionmaker(bind=engine)


#==================================
# Define Database with Metadata
#==================================

metadata = MetaData()

users = Table( 'users', metadata,
               Column('id', Integer, primary_key=True),
               Column('name', String),
               Column('fullname', String) )

addresses = Table( 'addresses', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('user_id', None, ForeignKey('users.id')),
                   Column('email_addresses', String, nullable=False) )

name_column = [ users.columns.name,
                users.c.name,
                users.c['name'] ]

fks = users.foreign_keys
pks = users.primary_key

assert users.metadata is metadata
assert users.bind is engine



#=========================
# Create Database
#=========================

for table in metadata.sorted_tables:
    table.create(engine)
    table.drop(engine)

metadata.create_all(engine)

#=========================
# Bind with ORM
#=========================
    
class User(Base):
    __table__ = 'users'
    
    id = Column()
    name = Column()
    fullname = Column()
    password = Column()

    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password
    
    def _repr__(self):
        pass
    
#=========================
# Access Database
#=========================

session = Session()    

some_user = User()
session.add(some_user)

our_user = session.query(User).filter_by(name='ed').first()

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

#=========================
    
if __name__ == '__main__':
    pass
