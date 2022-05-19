'''Тернарный оператор'''
# возвращает 1 или 3 операнд в зависимости от логики
# результат 1 если выражение_истинно иначе результат 2
import random

is_has_name = True
name = 'Alex' if is_has_name else 'Empty'
print(name)


is_one = False
number = 99 if is_one else 1
print(number)


is_russian = True
print('White' if is_russian else 'Black')

'''Задача 1.1 слово -> СлОвО'''


word = 'слово'
result = []

for i in range(len(word)):
#     if i % 2 != 0:
#         letter = word[i].lower()
#     else:
#         letter = word[i].upper()
    letter = word[i].lower() if i % 2 != 0 else word[i].upper()
    result.append(letter)

result = ''.join(result)
print(result)

'''Задача 1.2. Проверить пароль'''

password = input('Введите пароль: ')
print('Войти' if password == 'office' else 'Неверный пароль')


''' Генераторы '''
# вместо цикла for
# [number for number in numbers if number > 0]

# генератор списка
numbers = [1, 2, 3, 4, 5, -1, -2, 3]
result = [number for number in numbers if number > 0]
print(result)

# генератор словая

pairs = [(1, 'a'), (2, 'b'), (3, 'l')]
print(pairs)
result = {pair[0]: pair[1] for pair in pairs}
print(result)


'''Задача 2.1'''

# Создать список из 10 случайных чисел от 1 до 100
numbers = [random.randint(0,100) for i in range(10)]
print(numbers)

# Создать список имён на букву 'A'

names = ['Alina', 'Bob', 'Asya', 'Mikle', 'Armen', 'Rudy']

names = [name for name in names if name.startswith('A')]
print(names)


'''Операторы and и or'''













