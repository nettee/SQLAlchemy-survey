#!/usr/bin/env python

from sqlalchemy import *
engine = create_engine('sqlite:///:memory:', echo=True)

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

ins = users.insert().values(name='Jack', fullname='Jack Jones')

conn = engine.connect()
result = conn.execute(ins)

ins = users.insert()
conn.execute(ins, id=2, name='Wendy', fullname='Wendy Williams')

conn.execute(addresses.insert(), [ 
        {'user_id': 1, 'email_address' : 'jack@yahoo.com'},
        {'user_id': 1, 'email_address' : 'jack@msn.com'},
        {'user_id': 2, 'email_address' : 'www@www.org'},
        {'user_id': 2, 'email_address' : 'wendy@aol.com'},
])

#s = select([users.c.name, users.c.fullname])
s = select([users, addresses])
result = conn.execute(s)
for row in result:
    print row
