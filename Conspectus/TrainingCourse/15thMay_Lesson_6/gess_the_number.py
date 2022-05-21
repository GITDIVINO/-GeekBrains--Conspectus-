'''Игра "Угадай число" '''
#Шаг 1. Компьютер загадывает число
import random

number = random.randint(1,100)
print(number)

#Шаг 1. Запрашивает число у пользователя
#user_number = int(input('Введите число: '))

#Шаг 3. Сравниваем загаданное и полученное от пользователя
'''if number == user_number:
    print('Победа')
elif number < user_number:
    print('Число должно быть меньше')
else number > user_number:
    print('Число должно быть больше')'''

#Шаг 4. Прописываем цикл для одного числа
while True:
    user_number = int(input('Введите число: '))
    if number == user_number:
        print('Победа')
        break
    elif number < user_number:
        print('Число должно быть меньше')
    else:
        print('Число должно быть больше')