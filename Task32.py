# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного максимума)

import random
# Задаем массив
def create_array(number_n):
    array = list()
    for i in range(number_n):
        array.append(random.randint(1, number_n+10))
    return array
# Выбираем нужные элементы и сохраняем в отдельном массиве.
def list_select(array, min_, max_):
    result = []
    for i in range(len(array)):
        if min_ < array[i] < max_ :
            result.append(i)
    return result

# Создаем массив, указываем границы.
number = int(input("Размер массива: "))
list_1 = create_array(number)
max_n = int(input("Верхняя граница диапазона: "))
min_n = int(input("Нижняя граница диапазона: "))

print(list_select(list_1, min_n, max_n))