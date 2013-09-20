#!/usr/bin/env python
# -*- utf-8 -*-
#------------------------------------------------
import sqlite3 as sqlite
import sys

#------------------------------------------------
# databse connection using try
#------------------------------------------------

con = None
try:
    con = sqlite.connect('test.db')
    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')
    data = cur.fetchone()
    print 'SQLite version: %s' % data
except sqlite.Error, e:
    print 'Error %s:' % e.args[0]
    sys.exit(1)
finally:
    if con:
        con.close()

#------------------------------------------------
# data definition
#------------------------------------------------

people = [
    {'name': 'a', 'id': 1, 'gender': 'female'},
    {'name': 'b', 'id': 2, 'gender': 'male'  },
    {'name': 'c', 'id': 3, 'gender': 'female'},
    {'name': 'd', 'id': 4, 'gender': 'male'  },]

#------------------------------------------------
# write database
#------------------------------------------------

con = sqlite.connect('test.db')
with con:
    cur = con.cursor()
    cur.execute(''' DROP TABLE IF EXISTS Cars ''')
    cur.execute(''' CREATE TABLE Cars(Id INT, Name TEXT, Price INT) ''')
    cur.execute(''' INSERT INTO Cars VALUES(1,'Audi',52642) ''')
    cur.execute(''' INSERT INTO Cars VALUES(2,'Mercedes',57127) ''')
    cur.execute(''' INSERT INTO Cars VALUES(3,'Skoda',9000) ''')
    cur.execute(''' INSERT INTO Cars VALUES(4,'Volvo',29000) ''')
    
    cur.executescript(
        ''' INSERT INTO Cars VALUES(5,'Audi',52642); '''
        ''' INSERT INTO Cars VALUES(6,'Mercedes',57127); '''
        ''' INSERT INTO Cars VALUES(7,'Skoda',9000); '''
        ''' INSERT INTO Cars VALUES(8,'Volvo',29000); ''')


    cur.executescript(
        '''DROP TABLE IF EXISTS People;'''
        '''CREATE TABLE People(name TEXT, id INT, gender TEXT); ''')

    insert_sql = (
        ''' INSERT INTO People (name, id, gender)'''
        ''' VALUES (%s, %d, %s)''')
    
    for p in people:
        cur.execute(insert_sql, (p['name'], p['id'], p['gender']))

#------------------------------------------------
# data query
#------------------------------------------------
    cur.execute('SELECT * FROM Cars')
    rows = cur.fetchall()
    for line in rows:
        print line

    cur.execute('SELECT * FROM People')
    rows = cur.fetchall()
    for line in rows:
        print line

