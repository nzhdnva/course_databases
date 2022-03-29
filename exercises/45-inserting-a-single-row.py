# pec
from sqlalchemy import (create_engine, MetaData, Table, Column, String,
                        Integer, Float, Boolean)
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
# Импорт insert и select из sqlalchemy
from sqlalchemy import insert, select

# Создайте инструкцию insert для вставки записи в таблицу: insert_stmt
insert_stmt = insert(data).values(name='Анна', count=1, amount=1000.00, valid=True)

# Выполните инструкцию insert через execute: results
results = connection.execute(insert_stmt)

# Количество строк результата печати
print(results.rowcount)

# Создайте оператор select для проверки вставки: select_stmt
select_stmt = select([data]).where(data.columns.name == 'Анна')

# Выведите результат выполнения запроса.
print(connection.execute(select_stmt).first())
