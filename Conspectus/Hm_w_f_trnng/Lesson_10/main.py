'''3: Создайте модуль main.py. Из модулей реализованных в заданиях 1 и 2 сделайте импорт в main.py всех функций.
Вызовите каждую функцию в main.py и проверьте что все работает как надо.
Примечание: Попробуйте импортировать как весь модуль целиком (например из задачи 1),
так и отдельные функции из модуля. '''
import random
from Lesson_10_ex_1.directory_maker import *
from Lesson_10_ex_2.random_num import *

make_directory()
delete_directory()

boom = []
a = 0
for i in range(1,101):
    a = random.randint(1,101)
    boom.append(a)

print(random_num(boom))










