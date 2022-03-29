from urllib.request import urlretrieve
from sqlalchemy import (create_engine, MetaData, Table, select, desc, func,
                        update, Column, String, insert)

filename = 'https://storage.yandexcloud.net/deepskills-datasets/census_fake.sqlite'
urlretrieve(filename, 'census.sqlite')
engine = create_engine('sqlite:///census.sqlite')
metadata = MetaData()
connection = engine.connect()
flat_census = Table('flat_census', metadata, Column('city_name', String(256)),
                    Column('circuit_code', String(256)))
metadata.create_all(engine)
census = Table('census', metadata, autoload=True, autoload_with=engine)
city_fact = Table('city_fact', metadata, autoload=True, autoload_with=engine)
circuit_codes = connection.execute(select([city_fact.columns.circuit_court])).fetchall()
values_list = []

for code in circuit_codes:
    values_list.append({'circuit_code': code.circuit_court})

connection.execute(insert(flat_census), values_list)

# Решение -----------------------------------------
# Напишите функцию для выбора name из city_fact: circuit_stmt
circuit_stmt = select([city_fact.columns.name])

# Добавьте метод where(), чтобы сопоставить circuit_court с flat_census circuit_code: circuit_stmt
circuit_stmt = circuit_stmt.where(
    city_fact.columns.circuit_court == flat_census.columns.circuit_code)

# Напишите функцию update(), чтобы задать name circuit_stmt_where: update_stmt
update_stmt = update(flat_census).values(city_name=circuit_stmt)

# Выполнить update_stmt: результаты
results = connection.execute(update_stmt)

# Вывести количество строк
print(results.rowcount)
