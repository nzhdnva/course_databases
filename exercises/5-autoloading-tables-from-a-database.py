# pec
from urllib.request import urlretrieve

filename = 'https://storage.yandexcloud.net/deepskills-datasets/census_fake.sqlite'
urlretrieve(filename, 'census.sqlite')


# Решение -----------------------------------------
# Импорт create_engine, MetaData и Table
from sqlalchemy import create_engine, MetaData, Table

# Создать движок: движок
engine = create_engine('sqlite:///census.sqlite')

# Создать объект MetaData: metadata
metadata = MetaData()

# Отразить таблицу переписи из движка: census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Печать metadata таблицы переписи
print(repr(census))
