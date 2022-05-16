'''3: Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
name - строка полученная от пользователя,
health = 100,
damage = 50. ### Поэкспериментируйте с значениями урона и жизней по желанию.
### Теперь надо создать функцию attack(person1, person2). Примечание: имена аргументов можете указать свои.
### Функция в качестве аргумента будет принимать атакующего и атакуемого. ### В теле функция должна получить
параметр damage атакующего и отнять это количество от health атакуемого. Функция должна сама работать со словарями
и изменять их значения.'''

#Задаём сущности с помощью словаря
player = {'name': input('Please enter first_player name: '), 'health': 1000, 'damage': 50}
enemy = {'name': input('Please enter second_player name: '), 'health': 1000, 'damage': 50}

#Выводим на экран текущие параметры каждого игрока
print(player['name'] + ' has ' + str(player['health']) + ' points of health and ' + str(player['damage']) + ' points of damage')
print(enemy['name'] + ' has ' + str(enemy['health']) + ' points of health and ' + str(enemy['damage']) + ' points of damage')

hit = None #Переменная, которая описывает куда будет нанесён удар

#Описываем функцию для атаки
def attack(unit_1,unit_2,hit):
    hit = input('Куда будет наннесён удар? ')

    if hit == 'head':
        unit_2['health'] -= 5 * unit_1['damage']
    elif hit == 'leg':
        unit_2['health'] -= 3 * unit_1['damage']
    elif hit == 'arm':
        unit_2['health'] -= 2 * unit_1['damage']


    if unit_2['health'] <= 0:
        print(unit_2['name'] + ' is DEAD')
        return False
    else:
        print(player['name'] + ' has ' + str(player['health']) + ' points of health')
        print(enemy['name'] + ' has ' + str(enemy['health']) + ' points of health')
        print('Fight continue........\n' + '_'*100 + '\n')

round = 0

while True:
    round += 1
    print(f'Round {round}')
    first_fighter = input('Кто наносит удар? ')
    if first_fighter == player['name']:
        unit_1 = player
        unit_2 = enemy
    if first_fighter == enemy['name']:
        unit_1 = enemy
        unit_2 = player

    attack(unit_1,unit_2,hit)





