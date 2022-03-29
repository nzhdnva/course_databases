# pec
from urllib.request import urlretrieve
from sqlalchemy import create_engine, MetaData, Table, select

filename = 'https://storage.yandexcloud.net/deepskills-datasets/census_fake.sqlite'
urlretrieve(filename, 'census.sqlite')
engine = create_engine('sqlite:///census.sqlite')
metadata = MetaData()
connection = engine.connect()
census = Table('census', metadata, autoload=True, autoload_with=engine)
city_count = {}
more_results = True
stmt = select([census]).limit(1000)
# Execute the connection and store the ResultProxy
results_proxy = connection.execute(stmt)

# Решение -----------------------------------------
# Запустите цикл while, проверяющий дополнительные результаты
while more_results:
    # Извлеките первые 50 результатов из ResultProxy: partial_results
    partial_results = results_proxy.fetchmany(50)

    # если список пуст, установите для more_results значение False
    if partial_results == []:
        more_results = False

    # Повторите цикл по извлеченным записям и увеличьте количество для city
    for row in partial_results:
        if row.city in city_count:
            city_count[row.city] += 1
        else:
            city_count[row.city] = 1

# Закройте ResultProxy и, следовательно, соединение
results_proxy.close()

# Вывести city_count
print(city_count)