'''У вас есть массив чисел, составьте из
них максимальное число.
Например: [61, 228, 9] -> 961228'''

import random

rand_list = [random.randint(1,300) for i in range(5)]
print(f'Список из {len(rand_list)} случайных чисел: {rand_list}')

def biggest_figure(some_list):
    all_figures = []
    for i in some_list:


biggest_figure(rand_list)





