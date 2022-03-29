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
# Удалить таблицы city_fact
city_fact.drop(engine)

# Проверьте, существует ли city_fact
print(city_fact.exists(engine))

# Удалить все таблицы
metadata.drop_all(engine)

# Проверьте, существует ли census
print(census.exists(engine))
