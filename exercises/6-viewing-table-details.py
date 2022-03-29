# pec
from urllib.request import urlretrieve

filename = 'https://storage.yandexcloud.net/deepskills-datasets/census_fake.sqlite'
urlretrieve(filename, 'census.sqlite')

# Решение -----------------------------------------
from sqlalchemy import create_engine, MetaData, Table

engine = create_engine('sqlite:///census.sqlite')

metadata = MetaData()

# Отобразить таблицу census из движка: census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Вывести имена столбцов
print(census.columns.keys())

# Печать полных метаданных переписи
print(repr(metadata.tables['census']))
