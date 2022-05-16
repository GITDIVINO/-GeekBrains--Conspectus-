'''2: Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.'''

#v.1.0 Находим максимальное число, введённых от пользователя
# def choose_number():
#     List_of_numbers = [] #объявляем список, куда будем заносить числа
#
#     first_number = input('Введите первое число: ')
#     List_of_numbers.append(first_number) #добавляем в список
#     second_number = input('Введите второе число: ')
#     List_of_numbers.append(second_number)
#     third_number = input('Введите третье число: ')
#     List_of_numbers.append(third_number)
#     max_number = max(List_of_numbers) #вычисляем максимальное число
#     return max_number
#
#
# print(f'\nМаксимальное число из введённых: {choose_number()}')

#v.2.0 #Находим максимальное число из 3х чисел принимающих функция на вход
# def max_number(a,b,c):
#     numbers_list = []
#     numbers_list.append(a) #добавляем в список
#     numbers_list.append(b)
#     numbers_list.append(c)
#     number_max = max(numbers_list)
#     return number_max
#
# print(max_number(45,32,98))


#v.3.0 Тот же принцип, но с неограниченным количеством входящих аргументов
numbers_list = [] #объявляем список, куда будем заносить числа

print('Введите необходимое количество чисел и я вычислю наибольшее. Введите цифру "0" чтобы остановить ввод\n' + '_'*100) #инструкция для пользователя

while True: #цикл, запрашиввающий числа у пользователя и вносящий их в список
    number = int(input('Введите число: '))
    if number == 0:
        break
    else:
        numbers_list.append(number)

print('_'*100 + f'\nКоличество введёных чисел: {len(numbers_list)} ({numbers_list})')

def max_number(numbers_list): #та самая функция, которая делает магию
    number_max = max(numbers_list)
    return number_max

print(f'Наибольшее из них: {max_number(numbers_list)}')












