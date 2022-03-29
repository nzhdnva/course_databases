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

# Создайте инструкцию для очистки таблицы census: delete_stmt
delete_stmt = delete(census)

# Выполнить инструкцию: results
results = connection.execute(delete_stmt)

# Печать затронутого количества строк
print(results.rowcount)

# Создайте инструкцию для выбора всех записей из таблицы census : select_stmt
select_stmt = select([census])

# Выведите результаты выполнения инструкции, чтобы убедиться в отсутствии строк
print(connection.execute(select_stmt).fetchall())
