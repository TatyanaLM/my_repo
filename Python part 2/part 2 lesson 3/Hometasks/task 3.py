"""Задача 3: Написать программу, которая принимает на вход список чисел и с помощью декоратора выводит
время выполнения функции, которая сортирует его по возрастанию."""

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time elapsed: {(end_time-start_time)*1000:.6f} ms")
        return result
    return wrapper

@timer
def sort_numbers(numbers_list):
    return sorted(numbers_list)

numbers = [9, 3, 2, 1, 6, 8, 7, 5, 4]
print(sort_numbers(numbers))
