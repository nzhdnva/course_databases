# pec

# Решение -----------------------------------------
# Импорт create_engine, MetaData
from sqlalchemy import create_engine, MetaData

# Определите движок для подключения к chapter5.sqlite: engine
engine = create_engine('sqlite:///chapter5.sqlite')

# Инициализировать MetaData: metadata
metadata = MetaData()
