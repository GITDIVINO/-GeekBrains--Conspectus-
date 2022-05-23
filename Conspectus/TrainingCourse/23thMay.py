'''Необходимо найти число из спписка больше 5'''

import random
# объявляем список и заполняем его рандомными числами
rand_list = []

for i in range(0, 10):
    rand_list.append(random.randint(1, 15))
# выводим этот список на экран
print('Первый рандомный лист: ', rand_list)

# прописываем функцию, которая будет вытаскивать из нашего списка числа больше 5
def more_than_five(lst):
    result_list = []
    a = 0
    for i in lst:
        if lst[a] > 5:
            result_list.append(i)
        a += 1
    return result_list

# вызываем функцию и выводим значения в виде списка
print('Первая выборка >5 из 1 рандомного листа: ', more_than_five(rand_list))

#________________________________________________________________________________________________________________

'''переписываем код более лаконично'''

rand_list_2 = [random.randint(1, 15) for i in range(0, 10)]
print('\nВторой рандомный лист: ', rand_list_2)


def more_than_five_2(lst):
    result_list = [i for i in lst if i > 5]
    return result_list


print(f'Вторая выборка >5 из 2 рандомного листа: {more_than_five_2(rand_list_2)}')

#________________________________________________________________________________________________________________

'''Кусок кода из игры'''

# цикл будет заново запрашивать ввести да или нет до тех пор, пока не введут именно эти значения
def choise():
    choise = None
    while choise != 'yes' and choise != 'no':
        choise = input('Make your choise (yes or no): ')
    return choise


print(f'Your choise \'{choise()}\'')


