

# Решение -----------------------------------------
# Импорт функции create_engine
from sqlalchemy import create_engine

# Создать механизм для базы данных переписи
engine = create_engine('postgresql+psycopg2://student:datacamp@postgresql.csrrinzqubik.us-east-1.rds.amazonaws.com:5432/census')

# Используйте метод .table_names() в движке для печати имен таблиц
print(engine.table_names())