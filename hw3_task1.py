# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

import random
n = int(input("Введите количество элементов массива:"))
a = [random.randint(-10, 10) for i in range(n)]
print(a)
x = int(input("Введите число X:"))
print(a.count(x))
