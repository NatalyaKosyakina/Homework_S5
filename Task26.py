# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

def exponention(num_a, num_b):
    if num_b < 2:
        return num_a
    return exponention(num_a, num_b - 1) * num_a


num_a = int(input("А = "))
num_b = int(input("В = "))

print(f" -> {exponention(num_a, num_b)}")