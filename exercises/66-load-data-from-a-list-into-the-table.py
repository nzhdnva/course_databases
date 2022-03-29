# pec
import csv
from urllib.request import urlretrieve
from sqlalchemy import (create_engine, MetaData, Table, Column, String,
                        Integer)

filename = 'https://storage.yandexcloud.net/deepskills-datasets/census_fake.csv'
urlretrieve(filename, 'census.csv')
csvfile = open('census.csv', 'r')
csv_reader = csv.reader(csvfile)

engine = create_engine('sqlite:///:memory:')
metadata = MetaData()
census = Table('census', metadata,
               Column('city', String(30)), Column('sex', String(1)),
               Column('age', Integer()), Column('pop2013', Integer()),
               Column('pop2021', Integer())
)
metadata.create_all(engine)
connection = engine.connect()
values_list = []
for row in csv_reader:
    data = {'city': row[0], 'sex': row[1], 'age': row[2], 'pop2013': row[3],
            'pop2021': row[4]}
    values_list.append(data)

# Решение -----------------------------------------
# Импорт insert
from sqlalchemy import insert

# Функция insert(): stmt
stmt = insert(census)

# Используйте values_list для вставки данных: results
results = connection.execute(stmt, values_list)

# Вывести количество строк
print(results.rowcount)
