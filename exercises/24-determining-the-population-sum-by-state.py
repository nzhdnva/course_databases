# pec
from urllib.request import urlretrieve
from sqlalchemy import create_engine, MetaData, Table, select, desc

filename = 'https://storage.yandexcloud.net/deepskills-datasets/census_fake.sqlite'
urlretrieve(filename, 'census.sqlite')
engine = create_engine('sqlite:///census.sqlite')
metadata = MetaData()
connection = engine.connect()
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Решение -----------------------------------------
# Импорт func
from sqlalchemy import func

# Постройте выражение для вычисления суммы pop2021, помеченной как population
pop2021_sum = func.sum(census.columns.pop2021).label('population')

# Создайте запрос для выбора city и суммы pop2021: stmt
stmt = select([census.columns.city, pop2021_sum])

# Группировать stmt по городам
stmt = stmt.group_by(census.columns.city)

# Выполните execute и сохраните все записи: results
results = connection.execute(stmt).fetchall()

# Распечатайте results
print(results)

# Выведите keys/column возвращаемых результатов
print(results[0].keys())