# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d. Каждое число вводится с новой строки.

def arithmetic_progression(a1, d, n):
    an = []
    i = 1
    while i <= n:
        an.append(a1 + (i - 1) * d)
        i += 1
    return an

def print_el(list):
    for i in list:
        print(i)

first_el = int(input("Введите первый элемент: "))
difference = int(input("Введите разность: "))
items = int(input("Введите количество элементов: "))
array = arithmetic_progression(first_el, difference, items)
print_el(array)