# pec
from urllib.request import urlretrieve

filename = 'https://storage.yandexcloud.net/deepskills-datasets/census_fake.sqlite'
urlretrieve(filename, 'census.sqlite')

# Решение -----------------------------------------
from sqlalchemy import create_engine
engine = create_engine('sqlite:///census.sqlite')

# Создать соединение на движке
connection = engine.connect()

# Построить оператор выбора для таблицы переписи: stmt
stmt = 'SELECT * FROM census'

# Выполните инструкцию и извлеките результаты: results
results = connection.execute(stmt).fetchall()

# Распечатайте результат
print(results)