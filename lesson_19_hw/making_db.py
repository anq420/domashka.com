from sqlalchemy import (create_engine, MetaData, Table, Integer, String, Column, CheckConstraint)
from sqlalchemy.orm import Session


metadata = MetaData()
engine = create_engine('postgresql+psycopg2://anq420:030499@localhost/lesson_19_hw_contract_first')
ses = Session(bind=engine)


users = Table(
    'users', metadata,

    Column('id', Integer(), primary_key=True),
    Column('email', String(255), nullable=False, unique=True),
    Column('password', String, nullable=False),
    Column('nickname', String(255), nullable=False, unique=True),
    CheckConstraint("email LIKE '%@%' AND LOWER(email) = email", name='email_format_check')
)
metadata.create_all(engine)
