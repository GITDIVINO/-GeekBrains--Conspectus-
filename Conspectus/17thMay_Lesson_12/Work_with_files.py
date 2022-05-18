'''функция open открывает файл в указаном режиме
f = open('my.txt','w'), основные аргументы имя файла,
режим и кодировка '''
# r - чтение файла
#f = open('second.txt', 'r')
#f = open('first.txt', 'r')
# w - запись, если файла нет, создаётся новый
#f = open('first.txt', 'w')
# x - запись, если файла нет, ошибка
# a - дозапись
# b - двоичный режим
# + - открытие на чтение и запись

'''Запись текста в файл'''
# write - записать строку в файл
# writelines - записать список строк в файл
f = open('first.txt', 'w') #открыли файл для записи
#можем записывать по одной строчке
f.write('Hello ')
f.write('World!\n')

#или же записывать несколько строк сразу
f.writelines(['Mather ', 'Fucker'])

'''Чтение из файла'''
# read - чтение всего файла
f = open('first.txt', 'r')
#print(f.read())
#for line in f - чтение файла построчно
for line in f:
    print(line.replace('\n', ''))
#readines - чтение файла в список строк
#print(f.readlines())


'''Закрытие файлов'''
# f.close()
f.close()
# close() используя with
with open('first.txt', 'r') as f:
    for line in f:
        print(line.replace('\n', ''))
print('end')
#если использовать эту конструкцию, то f.close() использовать не надо
#файл закроется атоматически











