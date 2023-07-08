# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random

def find_index(n, m, list):
    for i in list:
        if i >= n and i <= m:
            print(list.index(i))

array = random.sample(range(1, 50), 10)
print(array)

min = int(input("Введите минимум: "))
max = int(input("Введите максимум: "))
find_index(min, max, array)