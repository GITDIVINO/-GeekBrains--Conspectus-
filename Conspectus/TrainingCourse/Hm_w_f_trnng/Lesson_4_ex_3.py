'''3: Дан список заполненный произвольными целыми числами.
Получите новый список, элементами которого будут только уникальные элементы исходного.
    Примечание. Списки создайте вручную, например так:
my_list_1 = [2, 2, 5, 12, 8, 2, 12]

В этом случае ответ будет:
[5, 8]'''

import random

his_list = []
unic_list = []

for i in range(100):
    his_list.append(random.randint(1,10))

print(f'Неуникальный список длиной {len(his_list)} символов: {his_list}')

for i in his_list:
    if i not in unic_list:
        unic_list.append(i)


print(f'Уникальный список длиной {len(unic_list)} символов: {unic_list}')









