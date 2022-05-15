'''Игра "Угадай число" с ограниченным количеством попыток'''
#Шаг 1. Компьютер загадывает число
import random


number = random.randint(1,100)
print(number)


user_number = None
count = 0 #переменная для подсчёта количества попыток
'max_count = 3 #максимальное количество попыток в игре'
levels = {1:10, 2:5, 3:3} #уровни сложности игры
level = int(input('Выберете уровень сложности (от 1 до 3): '))
max_count = levels[level] #максимально кол-во попыток зависит от уровня сложности


#Шаг 4. Прописываем цикл для одного числа
while number != user_number:
    count +=1
    if count > max_count:
        print('Вы проиграли')
        break
    print(f'Попытка № {count}')
    user_number = int(input('Введите число: ')) #Шаг 1. Запрашивает число у пользователя
    # Шаг 3. Сравниваем загаданное и полученное от пользователя
    if number < user_number:
        print('Число должно быть меньше')
    elif number > user_number:
        print('Число должно быть больше')
else:
    print('Победа')









