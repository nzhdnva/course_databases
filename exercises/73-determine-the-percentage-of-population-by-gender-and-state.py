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
# импортируйте case, cast и Float из sqlalchemy
from sqlalchemy import case, cast, Float

# Создайте запрос для расчета процента женщин в 2013 году: stmt
stmt = select([census.columns.city,
    (func.sum(
        case([
            (census.columns.sex == 'F', census.columns.pop2013)
        ], else_=0)) /
     cast(func.sum(census.columns.pop2013), Float) * 100).label('percent_female')
])

# Группировка по city
stmt = stmt.group_by(census.columns.city)

# Выполнить запрос и сохранить результаты: results
results = connection.execute(stmt).fetchall()

# Выведите процентное значение
for result in results:
    print(result.city, result.percent_female)
