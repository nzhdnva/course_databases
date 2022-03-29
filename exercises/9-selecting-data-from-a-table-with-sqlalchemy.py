# pec
from urllib.request import urlretrieve
from sqlalchemy import create_engine, MetaData, Table

filename = 'https://storage.yandexcloud.net/deepskills-datasets/census_fake.sqlite'
urlretrieve(filename, 'census.sqlite')
engine = create_engine('sqlite:///census.sqlite')
metadata = MetaData()
connection = engine.connect()

# Решение -----------------------------------------
# Импорт select
from sqlalchemy import select

# Отобразите таблицу переписи с помощью движка: census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Напишите оператор выбора для таблицы переписи: stmt
stmt = select([census])

# Выведите написанный оператор, чтобы увидеть строку SQL
print(stmt)

# Выполните инструкцию при подключении и извлеките 10 записей: results
results = connection.execute(stmt).fetchmany(size=10)

# Выполните инструкцию и распечатайте результаты
print(results)