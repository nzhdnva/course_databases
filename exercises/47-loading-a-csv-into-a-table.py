# pec
from urllib.request import urlretrieve
from sqlalchemy import (create_engine, MetaData, Table, Column, String,
                        Integer, Float, Boolean, insert)
import pandas as pd

filename = 'https://storage.yandexcloud.net/deepskills-datasets/census_fake.csv'
urlretrieve(filename, 'census.csv')

engine = create_engine('sqlite:///:memory:')
metadata = MetaData()
census = Table('census', metadata,
               Column('city', String(30)), Column('sex', String(1)),
               Column('age', Integer()), Column('pop2013', Integer()),
               Column('pop2021', Integer())
)
metadata.create_all(engine)
connection = engine.connect()

# Решение -----------------------------------------
