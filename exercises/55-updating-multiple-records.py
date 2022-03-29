# pec
from urllib.request import urlretrieve
from sqlalchemy import (create_engine, MetaData, Table, select, desc, func,
                        update)

filename = 'https://storage.yandexcloud.net/deepskills-datasets/census_fake.sqlite'
urlretrieve(filename, 'census.sqlite')
engine = create_engine('sqlite:///census.sqlite')
metadata = MetaData()
connection = engine.connect()
census = Table('census', metadata, autoload=True, autoload_with=engine)
city_fact = Table('city_fact', metadata, autoload=True, autoload_with=engine)

# Решение -----------------------------------------
# Напишите функцию для обновления note "Город отличных разработчиков": stmt
stmt = update(city_fact).values(note="Город отличных разработчиков")

# Добавьте метод where() для сопоставления записей: stmt_city
stmt_city = stmt.where(city_fact.columns.type == 'city')

# Выполнить инструкцию: результаты
results = connection.execute(stmt_city)

# Вывести количество строк
print(results.rowcount)