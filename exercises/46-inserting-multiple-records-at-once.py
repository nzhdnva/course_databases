# pec
from sqlalchemy import (create_engine, MetaData, Table, Column, String,
                        Integer, Float, Boolean, insert)
engine = create_engine('sqlite:///:memory:')
metadata = MetaData()
data = Table('data', metadata,
             Column('name', String(255)),
             Column('count', Integer()),
             Column('amount', Float()),
             Column('valid', Boolean())
)
metadata.create_all(engine)
connection = engine.connect()

# Решение -----------------------------------------
# Создайте список словарей: values_list
values_list = [
    {'name': 'Анна', 'count': 1, 'amount': 1000.00, 'valid': True},
    {'name': 'Михаил', 'count': 1, 'amount': 750.00, 'valid': False}
]

# Напишите insert() для таблицы данных: stmt
stmt = insert(data)

# Выполнить stmt с помощью values_list: results
results = connection.execute(stmt, values_list)

# Вывести количество строк
print(results.rowcount)
