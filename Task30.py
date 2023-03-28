# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Каждое число вводится с новой строки.
# Формула для получения n-го члена прогрессии: 
# an = a1 + (n-1) * d.

# Функция заполнения массива членами арифметической прогрессии
def arifmetic_progress_list(size, diff, first):
    array = [first]
    for i in range(1, size):
        array.append(first + i * diff)
    return array


# Ввод данных пользователем
size_m = int(input("Длина массива: "))
diff_m = int(input("Разность: "))
first_m = int(input("Первый элемент: "))

# Вызов функции и вывод результата
print(arifmetic_progress_list(size_m, diff_m, first_m))