# pec
from urllib.request import urlretrieve
from sqlalchemy import (create_engine, MetaData, Table, select, desc, func,
                        update, delete, and_)

filename = 'https://storage.yandexcloud.net/deepskills-datasets/census_fake.sqlite'
urlretrieve(filename, 'census.sqlite')
engine = create_engine('sqlite:///census.sqlite')
metadata = MetaData()
connection = engine.connect()
census = Table('census', metadata, autoload=True, autoload_with=engine)
city_fact = Table('city_fact', metadata, autoload=True, autoload_with=engine)

# Решение -----------------------------------------
# Напишите функцию для подсчета записей, используя столбец age для мужчин ('M') возраста 36: count_stmt
count_stmt = select([func.count(census.columns.sex)]).where(
    and_(census.columns.sex == 'M',
         census.columns.age == 36)
)

# Выполните запрос select и используйте метод выборки scalar() для сохранения количества записей
to_delete = connection.execute(count_stmt).scalar()

# Напишите функцию для удаления записей из таблицы census: delete_stmt
delete_stmt = delete(census)

# Добавьте метод where() для выбора мужчин ('M') в возрасте 36 лет: delete_stmt
delete_stmt = delete_stmt.where(
    and_(census.columns.sex == 'M',
         census.columns.age == 36)
)

# Выполнить инструкцию: results
results = connection.execute(delete_stmt)

# Выведите количество строк и количество записей to_delete, убедитесь, что они совпадают
print(results.rowcount, to_delete)
