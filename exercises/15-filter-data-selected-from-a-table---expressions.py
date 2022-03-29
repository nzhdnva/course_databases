# pec
from urllib.request import urlretrieve
from sqlalchemy import create_engine, MetaData, Table, select

filename = 'https://storage.yandexcloud.net/deepskills-datasets/census_fake.sqlite'
urlretrieve(filename, 'census.sqlite')
engine = create_engine('sqlite:///census.sqlite')
metadata = MetaData()
connection = engine.connect()
census = Table('census', metadata, autoload=True, autoload_with=engine)


# Решение -----------------------------------------
# Определите список городов, для которых мы хотим получить результаты
cities = ['Статград', 'Дебагинг', 'Програминск']

# Создайте запрос для таблицы census: stmt
stmt = select([census])

# Добавьте оператор where() с выборкой cities
stmt = stmt.where(census.columns.city.in_(cities))

# Повторите цикл над ResultProxy и выведите город и его население в 2013 году
for result in connection.execute(stmt):
    print(result.city, result.pop2013)
