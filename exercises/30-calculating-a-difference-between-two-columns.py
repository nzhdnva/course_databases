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
# Построить запрос для возврата названий городов по разнице в численности населения с 2013 по 2021 год: stmt
stmt = select([census.columns.city, (census.columns.pop2021-census.columns.pop2013).label('pop_change')])

# Добавить group_by для city: stmt_grouped
stmt_grouped = stmt.group_by(census.columns.city)

# Отсортируйте по pop_change по убыванию: stmt_ordered
stmt_ordered = stmt_grouped.order_by(desc('pop_change'))

# Вернуть только 5 результатов: stmt_top5
stmt_top5 = stmt_ordered.limit(5)

# Используйте execute для выполнения stmt_top5 и получения всех результатов
results = connection.execute(stmt_top5).fetchall()

# Распечатайте изменение города и численности населения для каждой записи
for result in results:
    print('{}:{}'.format(result.city, result.pop_change))
