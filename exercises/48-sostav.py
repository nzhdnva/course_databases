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
# Импорт pandas 
import pandas as pd

# считывание census.csv в DataFrame : census_df
census_df = pd.read_csv("census.csv", header=None)

# переименовать столбцы census_df
census_df.columns = ['city', 'sex', 'age', 'pop2013', 'pop2021']