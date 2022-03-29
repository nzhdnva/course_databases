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
# Импортируйте func
from sqlalchemy import func

# Создайте запрос для выбора городов и подсчета возрастов по городам: stmt
stmt = select([census.columns.city, func.count(census.columns.age)])

# Сгруппируйте stmt по городам
stmt = stmt.group_by(census.columns.city)

# Выполните инструкцию и сохраните все записи: results
results = connection.execute(stmt).fetchall()

# Распечатайте results
print(results)

# Выведите keys/column возвращаемых результатов
print(results[0].keys())
