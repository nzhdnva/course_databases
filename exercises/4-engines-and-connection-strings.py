# pec
from urllib.request import urlretrieve
filename = 'https://storage.yandexcloud.net/deepskills-datasets/census_fake.sqlite'
urlretrieve(filename, 'census.sqlite')

# Решение -----------------------------------------
# Импорт create_engine
from sqlalchemy import create_engine

# Создайте движок, который подключается к файлу census.sqlite: engine
engine = create_engine('sqlite:///census.sqlite')

# Печать имен таблиц
print(engine.table_names())
