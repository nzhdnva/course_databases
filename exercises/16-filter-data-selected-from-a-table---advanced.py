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
# Импорт and_
from sqlalchemy import and_

# Создайте запрос для таблицы census: stmt
stmt = select([census])

# Добавьте метод() where, чтобы выбрать только записи, не относящиеся к мужчинам, из Статграда, используя and_
stmt = stmt.where(
    # город Статград с полом != 'M'
    and_(census.columns.city == 'Статград',
         census.columns.sex != 'M'
         )
)

# Повторите цикл на ResultProxy, выведите возраст и пол
for result in connection.execute(stmt):
    print(result.age, result.sex)
