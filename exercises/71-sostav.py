# pec
from urllib.request import urlretrieve
from sqlalchemy import create_engine, MetaData, Table

filename = 'https://storage.yandexcloud.net/deepskills-datasets/census_fake.sqlite'
urlretrieve(filename, 'census.sqlite')
engine = create_engine('sqlite:///census.sqlite')
metadata = MetaData()
connection = engine.connect()
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Решение -----------------------------------------
# Импорт select и func
from sqlalchemy import select, func

# Добавьте столбец age в функцию select
stmt = select([census.columns.sex,
  			   (func.sum(census.columns.pop2013 * census.columns.age) 
  					/ func.sum(census.columns.pop2013)).label('average_age')               
			  ])

# Группировка по sex
stmt = stmt.group_by(census.columns.sex)