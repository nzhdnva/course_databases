# pec
import csv
from urllib.request import urlretrieve

filename = 'https://storage.yandexcloud.net/deepskills-datasets/census_fake.csv'
urlretrieve(filename, 'census.csv')
csvfile = open('census.csv', 'r')
csv_reader = csv.reader(csvfile)

# Решение -----------------------------------------
# Создать пустой список: values_list
values_list = []

# Перебор строк
for row in csv_reader:
    # Создайте словарь со значениями
    data = {'city': row[0], 'sex': row[1], 'age': row[2], 'pop2013': row[3],
            'pop2021': row[4]}
    # Добавить словарь в список значений
    values_list.append(data)
