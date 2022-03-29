# pec
from sqlalchemy import create_engine, MetaData
engine = create_engine('sqlite:///chapter5.sqlite')
metadata = MetaData()

# Решение -----------------------------------------
# Импорт Table, Column, String и Integer
from sqlalchemy import Table, Column, String, Integer

# Создайте таблицу census: census
census = Table('census', metadata,
               Column('city', String(30)),
               Column('sex', String(1)),
               Column('age', Integer()),
               Column('pop2013', Integer()),
               Column('pop2021', Integer()))

# Создайте таблицу в базе данных
metadata.create_all(engine)
