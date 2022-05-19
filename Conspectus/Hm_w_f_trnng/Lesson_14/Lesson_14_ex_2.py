'''2: Дан список, заполненный произвольными числами. Получить список из элементов исходного, удовлетворяющих
следующим условиям:
- Элемент кратен 3,
- Элемент положительный,
- Элемент не кратен 4.

Примечание: Список с целыми числами создайте вручную в начале файла. Не забудьте включить туда отрицательные числа.
10-20 чисел в списке вполне достаточно.'''

import random

numbers_list = [random.randint(-30,30) for i in range(50)]
print(numbers_list)

# numbers_list = [-3, -4, -5, -1, -2, 0, 1, 3, 5, 9]
# print(type(numbers_list[2]))

new_list = [number for number in numbers_list if number > 0 and number % 3 == 0 and number % 4 != 0]
print(new_list)


















