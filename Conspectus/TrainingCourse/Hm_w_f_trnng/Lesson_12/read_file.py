# читаем данные из записанного файла в консоли

import pickle
import json

with open('group.dat', 'rb') as f:
    group = pickle.load(f)

print(group)

with open('group.json', 'r') as f:
    json_my_favourite_group = json.load(f)

print(json_my_favourite_group)








