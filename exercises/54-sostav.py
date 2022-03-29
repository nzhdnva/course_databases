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
select_stmt = select([city_fact]).where(city_fact.columns.name == 'Питонбург')
results = connection.execute(select_stmt).fetchall()
print(results)
print(results[0]['type'])

update_stmt = update(city_fact).values(type = "city")
update_stmt = update_stmt.where(city_fact.columns.name == 'Питонбург')
update_results = connection.execute(update_stmt)

# Снова выполните select_stmt и получите новые результаты
new_results = connection.execute(select_stmt).fetchall()

# Распечатать new_results
print(new_results)

# Выведите "type" для первой строки new_results
print(new_results[0]['type'])