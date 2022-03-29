# pec
from urllib.request import urlretrieve
from sqlalchemy import create_engine, MetaData, Table, select, desc

filename = 'https://storage.yandexcloud.net/deepskills-datasets/census_fake.sqlite'
urlretrieve(filename, 'census.sqlite')
engine = create_engine('sqlite:///census.sqlite')
metadata = MetaData()
connection = engine.connect()
census = Table('census', metadata, autoload=True, autoload_with=engine)
city_fact = Table('city_fact', metadata, autoload=True, autoload_with=engine)

# Решение -----------------------------------------
# Создайте запрос для выбора таблиц census и city_fact: stmt
stmt = select([census, city_fact])

# Добавьте метод select_from(), который включает соединение для census и city_fact
# в таблице census, столбец city совпадает с столбцом name в таблице city_fact
stmt_join = stmt.select_from(
    census.join(city_fact, census.columns.city == city_fact.columns.name))

# Выполните execute и получите первый результат: result
result = connection.execute(stmt_join).first()

# Перебираем ключи в результирующем объекте и выводим ключ и значение
for key in result.keys():
    print(key, getattr(result, key))
