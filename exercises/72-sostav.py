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

# Выберите пол и средний возраст, по численности населения 2013 года
stmt = select([(func.sum(census.columns.pop2013 * census.columns.age) 
  					/ func.sum(census.columns.pop2013)).label('average_age'),
               census.columns.sex
			  ])

# Группировка по sex
stmt = stmt.group_by(census.columns.sex)

# Выполните запрос и извлеките все результаты
results = connection.execute(stmt).fetchall()

# Выведите столбец пола и среднего возраста для каждого результата
for result in results:
    print(result.sex, result.average_age)