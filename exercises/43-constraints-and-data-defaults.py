# pec
from sqlalchemy import create_engine, MetaData

engine = create_engine('sqlite:///:memory:')
metadata = MetaData()

# Решение -----------------------------------------
# Импорт Table, Column, String, Integer, Float, Boolean из sqlalchemy
from sqlalchemy import Table, Column, String, Integer, Float, Boolean

# Определите новую таблицу с name, count, amount и valid: data
data = Table('data', metadata,
             Column('name', String(255), unique=True),
             Column('count', Integer(), default=1),
             Column('amount', Float()),
             Column('valid', Boolean(), default=False)
)

# Используйте metadata для создания таблицы
metadata.create_all(engine)

# Распечатать сведения о таблице
print(repr(metadata.tables['data']))
