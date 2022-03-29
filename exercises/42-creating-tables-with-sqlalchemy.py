# pec
from sqlalchemy import create_engine, MetaData

engine = create_engine('sqlite:///:memory:')
metadata = MetaData()

# Решение -----------------------------------------
# Импорт Table, Column, String, Integer, Float, Boolean из sqlalchemy
from sqlalchemy import Table, Column, String, Integer, Float, Boolean

# Определите новую таблицу с name, count, amount и valid: data
data = Table('data', metadata,
             Column('name', String(255)),
             Column('count', Integer()),
             Column('amount', Float()),
             Column('valid', Boolean())
)

# Используйте metadata для создания таблицы
metadata.create_all(engine)

# Печать сведений о таблице
print(repr(data))
