'''Консольный файловый менеджер'''

#Для начала нужно продумать сигнатуру функций (входные параметры)

import os

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


if __name__ == '__main__':#для того, что бы этот скрипт не выполнялся в другой программе
    create_file('text.dat')
    create_file('text.dat', 'some text')
    create_folder('new_fl')
    get_list()
    get_list(True)


















