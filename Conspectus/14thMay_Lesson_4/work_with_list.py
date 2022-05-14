friends = ['Hulk', 'Stark', 'Vision', 'Tanos']
print(type(friends))

#Выведем длину списка
print(len(friends))

#Выведем добавляем новый элемент
print(friends)
friends.append('Vanda')
print(friends)

'''
friends.pop() #удаляем последний элемент
friends.clear() #очищаем список
friends.remove('Vanda') #удалить объекта из списка
del friends[3] # удалить элемент по индексу
'''
#Проверяем есть ли елемент в последовательность
String = 'Crypto'
List = ['Crypto', 'NYM', 'LUNA']
Cortege = ('Crypto', 'NYM', 'LUNA')

if 'r' in String:
    print('В строке есть "r"')
if 'NYM' in List:
    print('В листе есть "NYM"')
if 'LUNA' in Cortege:
    print('В кортедже есть "LUNA"')

#Перебираем строку с помощью While
i = 0
while i < len(String):
    Letter = String[i]
    print(Letter)
    i +=1

#Перебираем строку с помощью for
for Letter in String:
    print(Letter)

for i in List:
    print(i)

#использование range

numbers = range(10)
print(numbers)
print(list(numbers))

#range принимает три аргумента
for i in range(1,10,2):
    print(i)


#Словари dict
Hotel = {
    'room345': 'Bob',
    'room567': 'Chack',
    'room666': 'My girlfriend`s Mom'
}

print(Hotel)

#Добавляем ещё одну комнату в словарь
Hotel['room908'] = 'Who is here?'

print(Hotel)


#Удаляем элемент из словаря
del Hotel['room345']

print(Hotel)

#Перебераем словарь по ключу
for key in Hotel.keys():
    print(key)


#Множества (неупорядочная коллекция без повторения)

cities = ['Moscow', 'New York', 'London', 'Yasniy', 'Moskow']
print(cities)
print(type(cities))

cities = set(cities)
print(cities)
print(type(cities))




