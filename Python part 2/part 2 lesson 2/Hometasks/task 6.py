
"""Задача: Написать программу, которая принимает на вход список целых чисел и удаляет из него все нечетные числа.
При этом использовать только базовые операции, цикл for, функции и контейнерные типы данных."""

def remove_odd_numbers(lst):
    new_lst = []
    for i in lst:
        if i % 2 == 0:
            new_lst.append(i)
    return new_lst

print("Результат:", remove_odd_numbers([10, 11, 12, 13, 14]))

assert remove_odd_numbers([1, 2, 3, 4, 5]) == [2, 4]
assert remove_odd_numbers([10, 11, 12, 13, 14]) == [10, 12, 14]
assert remove_odd_numbers([2, 4, 6, 8, 10]) == [2, 4, 6, 8, 10]