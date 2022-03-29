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
# Построить запрос для возврата названия города и разницы в численности населения с 2013 по 2021 год
stmt = select([census.columns.city,
     (census.columns.pop2021-census.columns.pop2013).label('pop_change')
])

# Группировка по городам
stmt = stmt.group_by(census.columns.city)

# Порядок по изменению численности населения
stmt = stmt.order_by(desc('pop_change'))

# Ограничение до 10 лучших
#stmt = stmt.limit(10)
#это не нужно, у нас всего 5 городов

# Используйте соединение для выполнения инструкции и получения всех результатов
results = connection.execute(stmt).fetchall()

# Распечатайте изменение города и численности населения для каждой записи
for result in results:
    print('{}:{}'.format(result.city, result.pop_change))