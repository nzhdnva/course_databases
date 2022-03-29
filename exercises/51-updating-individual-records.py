# pec
from urllib.request import urlretrieve
from sqlalchemy import (create_engine, MetaData, Table, select, desc, func,
                        update)

filename = 'https://storage.yandexcloud.net/deepskills-datasets/census_fake.sqlite'
urlretrieve(filename, 'census.sqlite')
engine = create_engine('sqlite:///census.sqlite')
metadata = MetaData()
connection = engine.connect()
census = Table('census', metadata, autoload=True, autoload_with=engine)
city_fact = Table('city_fact', metadata, autoload=True, autoload_with=engine)
connection.execute(
    update(city_fact).where(city_fact.columns.name=='New York'
        ).values(fips_city=0)
)

# Решение -----------------------------------------
