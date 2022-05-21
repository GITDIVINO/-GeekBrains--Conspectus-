'''1: Создать модуль music_serialize.py. В этом модуле определить словарь для вашей любимой музыкальной группы,
например:
my_favourite_group = {
‘name’: ‘Г.М.О.’,
‘tracks’: [‘Последний месяц осени’, ‘Шапито’],
‘Albums’: [{‘name’: ‘Делать панк-рок’,‘year’: 2016},
{‘name’: ‘Шапито’,‘year’: 2014}]}

С помощью модулей json и pickle сериализовать данный словарь в json и в байты, вывести результаты в терминал.
Записать результаты в файлы group.json, group.pickle соответственно. В файле group.json указать кодировку utf-8.'''

import pickle # импортируем модуль pickle для работы с файлами
import json #импортируем модуль json для работы с файлами

# объявляем словарь с данными
my_favourite_group = {
    'name': 'Г.М.О.',
    'tracks': ['Последний месяц осени', 'Шапито'],
    'Albums': [{'name': 'Делать панк-рок','year': 2016}, {'name': 'Шапито','year': 2014}]
}

# записываем в файл данные
with open('group.dat', 'wb') as f:
    pickle.dump(my_favourite_group, f)

print('Объект записан в group.dat')

with open('group.json', 'w', encoding = 'utf-8') as f:
    json_my_favourite_group = json.dump(my_favourite_group, f)

print('Объект записан в group.json')












