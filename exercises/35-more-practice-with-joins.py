# pec
from urllib.request import urlretrieve
from sqlalchemy import create_engine, MetaData, Table, select, desc, func

filename = 'https://storage.yandexcloud.net/deepskills-datasets/census_fake.sqlite'
urlretrieve(filename, 'census.sqlite')
engine = create_engine('sqlite:///census.sqlite')
metadata = MetaData()
connection = engine.connect()
census = Table('census', metadata, autoload=True, autoload_with=engine)
city_fact = Table('city_fact', metadata, autoload=True, autoload_with=engine)

# Решение -----------------------------------------
# Создайте запрос select с выбором city, суммой населения в 2021 и 
# и type из city_fact: stmt
stmt = select([
    census.columns.city,
    func.sum(census.columns.pop2021),
    city_fact.columns.type
])

# Добавить select_from для соединения таблиц census и city_fact по столбцам census city и city_fact name
stmt_joined = stmt.select_from(
    census.join(city_fact, census.columns.city == city_fact.columns.name)
)

# Добавить group_by для столбца city_fact name
stmt_grouped = stmt_joined.group_by(city_fact.columns.name)

# Выполните execute и получите результаты: results
results = connection.execute(stmt_grouped).fetchall()

# Повторите цикл над объектом результатов и распечатайте каждую запись.
for record in results:
    print(record)
