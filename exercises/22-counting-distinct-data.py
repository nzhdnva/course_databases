# pec
from urllib.request import urlretrieve
from sqlalchemy import create_engine, MetaData, Table, select, desc

filename = 'https://storage.yandexcloud.net/deepskills-datasets/census_fake.sqlite'
urlretrieve(filename, 'census.sqlite')
engine = create_engine('sqlite:///census.sqlite')
metadata = MetaData()
connection = engine.connect()
census = Table('census', metadata, autoload=True, autoload_with=engine)
from sqlalchemy.sql import func

# Решение -----------------------------------------
# Создайте запрос для подсчета значений различных городов: stmt
stmt = select([func.count(census.columns.city.distinct())])

# Выполните запрос и сохраните скалярный результат: distinct_city_count
distinct_city_count = connection.execute(stmt).scalar()

# Выведите значение distinct_city_count
print(distinct_city_count)
