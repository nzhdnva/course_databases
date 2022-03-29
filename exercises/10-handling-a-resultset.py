# pec
from urllib.request import urlretrieve
from sqlalchemy import create_engine, MetaData, Table, select

filename = 'https://storage.yandexcloud.net/deepskills-datasets/census_fake.sqlite'
urlretrieve(filename, 'census.sqlite')
engine = create_engine('sqlite:///census.sqlite')
metadata = MetaData()
connection = engine.connect()
census = Table('census', metadata, autoload=True, autoload_with=engine)
stmt = select([census])
results = connection.execute(stmt).fetchmany(size=10)

# Решение -----------------------------------------
# Получите первую строку результатов с помощью индекса: first_row
first_row = results[0]

# Вывод первой строки результатов
print(first_row)

# Выведите первый столбец первой строки, обратившись к нему по его индексу
print(first_row[0])

# Выведите столбец city первой строки, используя его имя
print(first_row['city'])
