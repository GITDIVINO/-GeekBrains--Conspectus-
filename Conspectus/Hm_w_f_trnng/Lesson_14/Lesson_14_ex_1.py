'''1: Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.
    Примечание: Списки фруктов создайте вручную в начале файла.'''

first_fruits_list = [ 'Banan', 'Avocade', 'Apple', 'Orange', 'Pineapple', 'Melon']
second_fruits_list = ['Avocado', 'Orange', 'Igor', 'Donow', 'Melon', 'Banan']

#старый метод
# recurring_fruits = []
#
# for i in first_fruits_list:
#     for j in second_fruits_list:
#         if i == j:
#             recurring_fruits.append(i)
#
# print(recurring_fruits)

#по последним урокам [ number for number in numbers if number > 0 ]
recurring_fruits = [i for i in first_fruits_list for j in second_fruits_list if i == j ]
print(recurring_fruits)
























