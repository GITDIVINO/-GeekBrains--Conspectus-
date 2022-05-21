#Узнать длину строки
hero_name = 'Hulk'
print(len(hero_name))

#Найти слово/букву в строке
hero_phrase = 'Hulk like fire, Tor like water'
print(hero_phrase.find('fire'))

#Возвести в верхний регистр
print(hero_name.upper())

#Конкатенация

name = 'Тони'
age = 37

hello_str = 'Привет %s тебе %d лет'%(name,age)
print(hello_str)

hello_str = 'Привет {} тебе {} лет'.format(name, age)
print(hello_str)

#Необходимо из текста выделить информацию
top5 = 'Первые 5 мест по суперспособностям: 1.Ванда 2.Стрендж 3.Капитан Марвел 4.Ванда 5.Тор'

start = top5.find('1')
finish = top5.find('4')

top3 = top5[start: finish]

result = 'Топ самых сильных супергероев Марвел: {}'.format(top3.upper())

print(result)

