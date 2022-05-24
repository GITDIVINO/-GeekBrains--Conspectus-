'''У вас есть массив чисел. Напишите три функции, которые вычисляют сумму этих чисел:
с for-циклом, с while-циклом, с рекурсией.'''

import random

list = [random.randint(1, 100) for i in range(0, 10)]
print(f'Массив из {len(list)} случайных чисел: {list}')


# прописываем фукцию вычисления суммы с помощью цикла for
def sum_for(list):
    result = 0
    # result = [result  += i for i in list]
    for i in list:
        result += i
    return result


# вызываем функцию sum_for
print(f'Сумма элементов массива равна (for): {sum_for(list)}')


# прописываем фукцию вычисления суммы с помощью цикла while
def sum_while(list):
    i = 0
    result = 0
    while i < len(list):
        result += list[i]
        i += 1
    return result


# вызываем функцию sum_while
print(f'Сумма элементов массива равна (while): {sum_while(list)}')

# НЕ РЕШИЛ
# # прописываем фукцию вычисления суммы с помощью рекурсии
# def sum_rec(list, sum = 0):
#     intern_list = list
#     if len(intern_list) != 0:
#         sum += intern_list[0]
#         intern_list.pop(0)
#         # print(sum)
#         sum_rec(intern_list, sum)
#     else:
#         return sum
#
# # вызываем функцию sum_rec
# print(f'Сумма элементов массива равна (rec): {sum_rec(list)}')

#_______________________________________________________________________________

'''Напишите функцию, которая создаёт комбинацию двух списков таким образом:
[1, 2, 3] (+) [11, 22, 33] -> [1, 11, 2, 22, 3, 33]'''

def comb_list(list1,  list2):
    new_list = []
    i = 0
    for number in list1:
        new_list.append(list1[i])
        new_list.append(list2[i])
        i += 1
    return new_list

lst1 = [1, 2, 3]
lst2 = [11, 22, 33]
print(comb_list(lst1, lst2))

#________________________________________________________________________________

'''Вычислите первые 100 чисел Фибоначчи. (Напишите код.)'''

def fibo():
    how_many = input('Сколько чисел Фибоначчи нужно вывести? ')
    result = [0, 1]

    for i in range(int(how_many) - 2):
        result.append(int(result[-1]) + int(result[-2]))

    return print(f'Кличество элементов {len(result)} в списке Фибоначчи: {result}')

print(fibo())







