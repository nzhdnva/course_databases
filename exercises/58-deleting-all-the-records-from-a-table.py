# pec
from urllib.request import urlretrieve
from sqlalchemy import (create_engine, MetaData, Table)

filename = 'https://storage.yandexcloud.net/deepskills-datasets/census_fake.sqlite'
urlretrieve(filename, 'census.sqlite')
engine = create_engine('sqlite:///census.sqlite')
metadata = MetaData()
connection = engine.connect()
census = Table('census', metadata, autoload=True, autoload_with=engine)
city_fact = Table('city_fact', metadata, autoload=True, autoload_with=engine)

# Решение -----------------------------------------
# Импорт delete, select
from sqlalchemy import delete, select

# Напишите функцию для удаления таблицы census: delete_stmt
delete_stmt = delete(census)

# Выполнить инструкцию: results
results = connection.execute(delete_stmt)

# Печать количества строк
print(results.rowcount)

# Напишите функцию для выбора всех записей из таблицы census : select_stmt
select_stmt = select([census])

# Выведите результаты выполнения, чтобы убедиться в отсутствии строк
print(connection.execute(select_stmt).fetchall())
