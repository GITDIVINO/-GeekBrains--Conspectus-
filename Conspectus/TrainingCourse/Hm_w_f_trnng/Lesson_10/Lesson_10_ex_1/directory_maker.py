'''1: Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py). В нем создайте функцию создающую
директории от dir_1 до dir_9 в папке из которой запущен данный код. Затем создайте вторую функцию удаляющую эти папки.
Проверьте работу функций в этом же модуле.'''

import os #Импортируем модуль os

#Выводим текущую рабочую дирректорию
# path = os.getcwd()
# print ("Текущая рабочая директория %s" % path)

#прописываем путь где мы будем создавать дирректории
#path = 'C:/Users/User/Desktop/GeekBrains/Conspectus/Hm_w_f_trnng/Lesson_10_ex_1/1st'

def make_directory(): #прописываем функцию которая будет создавать дирректории
    for i in range(1,10):
        new_path = 'C:/Users/User/Desktop/GeekBrains/Conspectus/Hm_w_f_trnng/Lesson_10/{}_folder'.format(i)
        os.mkdir(new_path)

def delete_directory():
    for i in range(1,10):
        new_path = 'C:/Users/User/Desktop/GeekBrains/Conspectus/Hm_w_f_trnng/Lesson_10/{}_folder'.format(i)
        os.rmdir(new_path)


make_directory()
delete_directory()



