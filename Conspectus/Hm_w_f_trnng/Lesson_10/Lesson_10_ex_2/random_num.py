'''2: Создайте модуль. В нем создайте функцию, которая принимает список и возвращает из него случайный элемент.
Если список пустой функция должна вернуть None. Проверьте работу функций в этом же модуле.
    Примечание: Список для проверки введите вручную. Или возьмите этот: [1, 2, 3, 4]'''

import random

#List = [1,2,3,4]

def random_num(List):
    Rand_num = random.choice(List)
    if Rand_num == None:
        return None
    return Rand_num

#print(random_num(List))















