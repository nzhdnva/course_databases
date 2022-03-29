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
# Создайте запрос select: stmt
stmt = select([census])

# Добавьте предложение where в stmt, чтобы отфильтровать результаты только для Статградa : stmt_filtered
stmt = stmt.where(census.columns.city == 'Статград')

# Выполните запрос для получения всех возвращенных данных: результаты
results = connection.execute(stmt).fetchall()

# Зациклите результаты и выведите age, sex и pop2013
for result in results:
    print(result.age, result.sex, result.pop2013)
