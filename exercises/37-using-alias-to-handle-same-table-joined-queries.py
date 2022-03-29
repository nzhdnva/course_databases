# pec
from urllib.request import urlretrieve
from sqlalchemy import create_engine, MetaData, Table, select, desc, func

filename = 'https://storage.yandexcloud.net/deepskills-datasets/employees_fake.sqlite'
urlretrieve(filename, 'employees.sqlite')
engine = create_engine('sqlite:///employees.sqlite')
metadata = MetaData()
connection = engine.connect()
employees = Table('employees', metadata, autoload=True, autoload_with=engine)

# Решение -----------------------------------------
# Создайте псевдоним таблицы employees: managers
managers = employees.alias()

# Создайте запрос для выбора имен руководителей и их сотрудников: stmt
stmt = select(
    [managers.columns.name.label('manager'),
     employees.columns.name.label('employee')]
)

# Сопоставление идентификаторов руководителей с идентификаторами сотрудников mgr: stmt_matched
stmt_matched = stmt.where(managers.columns.id == employees.columns.mgr)

# Отсортируйте по имени руководителей: stm_ordered
stmt_ordered = stmt_matched.order_by(managers.columns.name)

# Выполнить инструкцию:
results = connection.execute(stmt_ordered).fetchall()

# Печать записей
for record in results:
    print(record)
