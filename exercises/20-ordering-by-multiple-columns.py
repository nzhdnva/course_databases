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
# Создайте запрос для выбора city и age: stmt
stmt = select([census.columns.city, census.columns.age])

# Добавить порядок, по возрастанию `city` и убыванию `age`
stmt = stmt.order_by(census.columns.city, desc(census.columns.age))

# Выполнить execute() и сохранить все записи: results
results = connection.execute(stmt).fetchall()

# Вывести первые 20 результатов
print(results[:20])
