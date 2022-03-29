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
# Создайте запрос для выбора столбца city: stmt
stmt = select([census.columns.city])

# Упорядочить stmt по столбцу city
stmt = stmt.order_by(census.columns.city)

# Выполнить запрос и сохранить результаты: results
results = connection.execute(stmt).fetchall()

# Вывести первые 10 результатов
print(results[:10])
