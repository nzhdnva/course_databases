# pec
from urllib.request import urlretrieve
from sqlalchemy import create_engine, MetaData, Table, select, desc, ForeignKeyConstraint

filename = 'https://storage.yandexcloud.net/deepskills-datasets/census_fake.sqlite'
urlretrieve(filename, 'census.sqlite')
engine = create_engine('sqlite:///census.sqlite')
metadata = MetaData()
connection = engine.connect()
census = Table('census', metadata, autoload=True, autoload_with=engine)
city_fact = Table('city_fact', metadata, autoload=True, autoload_with=engine)
census.append_constraint(ForeignKeyConstraint(['city'], ['city_fact.name']))

# Решение -----------------------------------------
# Создайте запрос для соединения таблиц census и city_fact: stmt
stmt = select([census.columns.pop2013, city_fact.columns.abbreviation])

# Выполните инструкцию и получите первый результат: result
result = connection.execute(stmt).first()

# Перебираем ключи в результирующем объекте и выводим ключ и значение
for key in result.keys():
    print(key, getattr(result, key))
