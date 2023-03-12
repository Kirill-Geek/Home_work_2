"""
Задача 14: Требуется вывести все целые степени двойки(т.е. числа вида 2k), 
не превосходящие числа N.
"""
num = int(input("Введите число n = "))
num_count = 2
while num_count <= num:
    print(num_count)
    num_count *=2