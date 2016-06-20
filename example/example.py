#!/usr/bin/env python

# encoding: utf-8

from sqlalchemy import *

engine = create_engine('sqlite:///:memory:', echo=False)

metadata = MetaData()
users = Table('users', metadata,
        Column('id', Integer, primary_key=True),
        Column('name', String),
        Column('fullname', String),
)
addresses = Table('addresses', metadata,
        Column('id', Integer, primary_key=True),
        Column('user_id', None, ForeignKey('users.id')),
        Column('email_address', String, nullable=False),
)

metadata.create_all(engine)

conn = engine.connect()

ins = users.insert().values(name='Jack', fullname='Jack Jones')
result = conn.execute(ins)

ins = users.insert()
conn.execute(ins, id=2, name='Wendy', fullname='Wendy Williams')

conn.execute(addresses.insert(), [ 
        {'user_id': 1, 'email_address' : 'jack@yahoo.com'},
        {'user_id': 1, 'email_address' : 'jack@msn.com'},
        {'user_id': 2, 'email_address' : 'www@www.org'},
        {'user_id': 2, 'email_address' : 'wendy@aol.com'},
])

for table in (users, addresses):
    print 'table %s' % str(table)
    s = select([table])
    result = conn.execute(s)
    for row in result:
        print row

result = conn.execute(select([addresses]))
for row in result:
    print row[addresses.c.email_address]
