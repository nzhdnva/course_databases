# pec
from urllib.request import urlretrieve
from sqlalchemy import create_engine, MetaData, Table, select, desc, func

filename = 'https://storage.yandexcloud.net/deepskills-datasets/census_fake.sqlite'
urlretrieve(filename, 'census.sqlite')
engine = create_engine('sqlite:///census.sqlite')
metadata = MetaData()
connection = engine.connect()
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Решение -----------------------------------------
# Импортируйте case, cast и Float из sqlalchemy
from sqlalchemy import case, cast, Float

# Постройте выражение для расчета численности женского населения в 2013 году
female_pop2013 = func.sum(
    case([
        (census.columns.sex == 'F', census.columns.pop2013)
    ], else_=0))

# Приведите выражение для вычисления общей численности населения в 2013 году к типу Float
total_pop2013 = cast(func.sum(census.columns.pop2013), Float)

# Создайте запрос для расчета процентной доли женщин в 2013 году: stmt
stmt = select([female_pop2013 / total_pop2013 * 100])

# Выполните запрос и сохраните скалярный результат: percent_female
percent_female = connection.execute(stmt).scalar()

# Выведите процентное значение
print(percent_female)
