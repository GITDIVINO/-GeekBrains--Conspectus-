'''3. Напишите функцию которая принимает на вход список. Функция создает из этого списка новый список из квадратных
корней чисел (если число положительное) и самих чисел (если число отрицательное) и возвращает результат (желательно
рименить генератор и тернарный оператор при необходимости). В результате работы функции исходный
список не должен измениться.
Например:
old_list = [1, -3, 4]
result = [1, -3, 2]

Примечание: Список с целыми числами создайте вручную в начале файла. Не забудьте включить туда отрицательные числа.
10-20 чисел в списке вполне достаточно.'''
import random

numbers_list = [random.randint(-50,50) for i in range(20)]
print(numbers_list)

def make_new_list(some_list):
    new_list = [i if i < 0 else i**2 for i in some_list]
    return new_list

print(make_new_list(numbers_list))

















