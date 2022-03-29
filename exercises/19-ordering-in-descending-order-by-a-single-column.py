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
# Импорт desc
from sqlalchemy import desc

# Создайте запрос для выбора столбца city: stmt
stmt = select([census.columns.city])

# Упорядочить stmt по состоянию в порядке убывания: rev_stmt
rev_stmt = stmt.order_by(desc(census.columns.city))

# Выполнить запрос и сохранить результаты: rev_results
rev_results = connection.execute(rev_stmt).fetchall()

# Вывести первые 10 результатов rev_results
print(rev_results[:10])
