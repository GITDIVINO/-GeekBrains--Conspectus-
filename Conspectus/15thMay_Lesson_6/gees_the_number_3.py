'''Игра "Угадай число" с ограниченным количеством попыток
и возможностью играть нескольким пользователям'''

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

user_count = int(input('Введите количество пользователей: '))
users = []
for i in range(user_count):
    user_name = input(f'Введите имя пользователя {i}: ')
    users.append(user_name)

print(users)

is_winner = False
winner_name = None

#Шаг 4. Прописываем цикл для одного числа
while not is_winner:
    count +=1
    if count > max_count:
        print('Все пользователи проиграли')
        break
    print(f'Попытка № {count}')

    #Прописываем ходы для каждого игрока
    for user in users:
        print(f'Ход пользователя {user}')
        user_number = int(input('Введите число: ')) #Шаг 1. Запрашивает число у пользователя
        if user_number == number:
            is_winner = True
            winner_name = user
            break
        # Шаг 3. Сравниваем загаданное и полученное от пользователя
        elif number < user_number:
            print('Число должно быть меньше')
        else:
            print('Число должно быть больше')
else:
    print(f'Победитель {winner_name}')









