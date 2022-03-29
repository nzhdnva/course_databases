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

# Создайте инструкцию для обновления type на "city": update_stmt
update_stmt = update(city_fact).values(type = "city")

# Добавьте предложение where, чтобы ограничить его записями для города Питонбург
update_stmt = update_stmt.where(city_fact.columns.name == 'Питонбург')

# Выполнить инструкцию update: update_results
update_results = connection.execute(update_stmt)