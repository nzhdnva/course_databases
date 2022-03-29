# pec
from urllib.request import urlretrieve
from sqlalchemy import create_engine, MetaData, Table, select, desc

filename = 'https://storage.yandexcloud.net/deepskills-datasets/census_fake.sqlite'
urlretrieve(filename, 'census.sqlite')
engine = create_engine('sqlite:///census.sqlite')
metadata = MetaData()
connection = engine.connect()
census = Table('census', metadata, autoload=True, autoload_with=engine)
from sqlalchemy.sql import func
stmt = select([census.columns.city,
               func.sum(census.columns.pop2021).label('population')]
    ).group_by(census.columns.city).order_by(desc('population')).limit(5)
results = connection.execute(stmt).fetchall()

# Решение -----------------------------------------
# Импорт pandas
import pandas as pd

# Создайте DataFrame данных из results: df
df = pd.DataFrame(results)

# Задать имена столбцов
df.columns = results[0].keys()

# Распечатать df
print(df)