#Определение функций с неограниченным количеством параметров

def greeting(say, *args):
    print(say, args)

greeting('Hello', 'Leo')


greeting('Hello', 'Leo', 'Max')
greeting('Hello', 'Leo', 'Max', 'Kate')



def get_person(**kwargs):
    for k,v in kwargs.items():
        print(k,v)

get_person(name = 'Leo', age = 20, has_car = True)


#Области видимости
'''В програмироввании это область программы, в пределах которой 
идентификатор (имя) некоторой переменной продолжает быть связаннм с этой
переменной и возвращать её занчение

За пределами области видимости тот же самый идентификатор
может быть связан с другой переменной, либо быть свободным '''

def my_func (my_var):
    my_var = 999
    print(f'Внутри функции переменная my_var имеет значение {my_var}')

a = 1
my_func(a)
print(f'После выполнение функции переменная a имеет значение {a}')




