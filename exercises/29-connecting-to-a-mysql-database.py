

# Решение -----------------------------------------
# Импорт функции create_engine
from sqlalchemy import create_engine

# Создать движок для базы данных census
engine = create_engine('mysql+pymysql://student:datacamp@courses.csrrinzqubik.us-east-1.rds.amazonaws.com:3306/census')

# Вывести имена таблиц
print(engine.table_names())
