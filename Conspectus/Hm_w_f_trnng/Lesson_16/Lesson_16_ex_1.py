'''1. В консольный файловый менеджер добавить проверку ввода пользователя для всех функции с параметрами
(на уроке разбирали на примере одной функции).'''

# что бы импортировать функции из модуля core мы должны задать путь через sys
import sys
sys.path.append('/mnt/c/Users/User/Desktop/GeekBrains/Conspectus/19thMay_Lesson_16')
from core import create_file, create_folder, get_list, delete_file, copy_file, save_info

save_info('start')
command = sys.argv[1]


if command == 'list':
    get_list()

elif command == 'create_file':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсутствует второй параметр')
    else:
        create_file(name)
        print(f'Файл с именем \"{name}\" создан')

elif command == 'create_folder':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсутствует второй параметр')
    else:
        create_folder(name)
        print(f'Папка с именем \"{name}\" создана')

elif command == 'delete_file':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсутствует второй параметр')
    else:
        delete_file(name)
        print(f'Файл\папка с именем \"{name}\" удалён(а)')

elif command == 'copy':
    try:
        name = sys.argv[2]
        new_name = sys.argv[3]
    except IndexError:
        print('Отсутствует второй или третий параметр')
    else:
        copy_file(name, new_name)
    print(f'Файо с именем \"{name}\" скопирована с именем \"{new_name}\"')
elif command == 'help':
    print('Вы можете воспользоваться следущими командами: ')
    print('list - список файлов и папок')
    print('create_file - создать файл')
    print('create_folder - создать директорию')
    print('delete_file - удалить файл')
    print('copy - скопировать (имя файла и новое имя')

save_info('finish')























