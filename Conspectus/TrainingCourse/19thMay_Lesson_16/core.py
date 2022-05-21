'''Консольный файловый менеджер'''

#Для начала нужно продумать сигнатуру функций (входные параметры)

import os
import shutil
import datetime

def create_file(name, text = None):
    with open(name, 'w', encoding = 'utf-8') as f:
        if text:
            f.write(text)


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Такая папка уже есть')


def get_list(folder_only = False):
    result = os.listdir()
    if folder_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


def delete_file(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)


def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Такая папка уже есть')
    else:
        shutil.copy(name, new_name)


def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    with open('log.txt', 'a', encoding = 'utf-8') as f:
        f.write(result + '\n')


def cwd(name):
    os.chdir(name)
    print('Вы изменили текущую дерректорию')


if __name__ == '__main__':#для того, что бы этот скрипт не выполнялся в другой программе
    create_file('text.dat')
    create_file('text.dat', 'some text')
    create_folder('new_fl')
    get_list()
    get_list(True)
    delete_file('new_fl')
    delete_file('text.dat')
    copy_file('new_fl', 'new_2')
    copy_file('text.dat', 'text_2.dat')
    save_info('booooom')
    cwd('/mnt/c/Users/User/Desktop/GeekBrains/Conspectus/')


















