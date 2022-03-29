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
# Создайте оператор select: select_stmt
select_stmt = select([city_fact]).where(city_fact.columns.name == 'Питонбург')

# Выполнить select_stmt и получить результаты
results = connection.execute(select_stmt).fetchall()

# Вывести результаты выполнения select_stmt
print(results)

# Выведите код type для первой строки результата
print(results[0]['type'])