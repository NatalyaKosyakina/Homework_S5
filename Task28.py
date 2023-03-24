# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def recursive_summ(num_a, num_b):
    if num_b == 0 :
        return num_a
    return recursive_summ(num_a + 1, num_b - 1)

num_a = int(input("А = "))
num_b = int(input("В = "))

print(f" -> {recursive_summ(num_a, num_b)}")