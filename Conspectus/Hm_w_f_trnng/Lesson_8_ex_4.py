'''4: Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр - armor = 1.2 (величина брони персонажа)
Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
Следовательно, у вас должно быть 2 функции:
Наносит урон. Это улучшенная версия функции из задачи 3.
Вычисляет урон по отношению к броне.

Примечание. Функция номер 2 используется внутри функции номер 1 для вычисления урона и вычитания его из здоровья персонажа. '''

#Задаём сущности с помощью словаря
player = {'name': input('Please enter first_player name: '), 'health': 1000, 'damage': 50, 'armor': 1.5}
enemy = {'name': input('Please enter second_player name: '), 'health': 1000, 'damage': 50, 'armor': 4.5}

#Выводим на экран текущие параметры каждого игрока
print(player['name'] + ' has ' + str(player['health']) + ' points of health and ' + str(player['damage']) + ' points of damage')
print(enemy['name'] + ' has ' + str(enemy['health']) + ' points of health and ' + str(enemy['damage']) + ' points of damage')

hit = None #Переменная, которая описывает куда будет нанесён удар

#Описываем функцию для атаки
def attack(unit_1,unit_2,hit):
    hit = input('Куда будет наннесён удар? ')

    if hit == 'head':
        a = 5
        unit_2['health'] -= defence(unit_2['armor'],unit_1['damage'],a) #Вызываем функцию, которая считает урон с бронёй
    elif hit == 'leg':
        b = 3
        unit_2['health'] -= defence(unit_2['armor'],unit_1['damage'],b)
    elif hit == 'arm':
        c = 2
        unit_2['health'] -= defence(unit_2['armor'],unit_1['damage'],c)


    if unit_2['health'] <= 0:
        print(unit_2['name'] + ' is DEAD')
        return False
    else:
        print(player['name'] + ' has ' + str(player['health']) + ' points of health')
        print(enemy['name'] + ' has ' + str(enemy['health']) + ' points of health')
        print('Fight continue........\n' + '_'*100 + '\n')

#Описываем функцию, которая уменьшает урон в зависимости от брони
def defence(armor,damage,a):
    a_damage = int((a * unit_1['damage'])/armor)
    return a_damage

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












