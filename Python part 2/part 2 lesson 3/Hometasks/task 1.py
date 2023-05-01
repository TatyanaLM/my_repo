
"""Задача 1: Написать программу, которая принимает на вход список чисел и
возвращает список, содержащий только нечетные числа, умноженные на два.
При этом, использовать функции filter, map и лямбда-функцию.
"""
"""Функция filter() в Python применяет другую функцию к заданному итерируемому объекту 
(список, строка, словарь и так далее), проверяя, нужно ли сохранить конкретный элемент или нет. 
Простыми словами, она отфильтровывает то, что не проходит и возвращает все остальное.
Функция filter() принимает два параметра. Первый — имя созданной пользователем функции, 
а второй — итерируемый объект (список, строка, множество, кортеж и так далее"""
def get_odd_doubled_numbers(numbers):
    result = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 1, numbers)))
    return result

def test_get_odd_doubled_numbers():
    assert get_odd_doubled_numbers([1, 2, 3, 4, 5]) == [2, 6, 10]
    assert get_odd_doubled_numbers([10, 20, 30]) == []
    assert get_odd_doubled_numbers([]) == []
    assert get_odd_doubled_numbers([1, 3, 5]) == [2, 6, 10]
    assert get_odd_doubled_numbers([2, 4, 6]) == []
    print("All test_get_odd_doubled_numbers passed!")

print(get_odd_doubled_numbers([1, 2, 3, 4, 5]))
print(get_odd_doubled_numbers([10, 20, 30]))
print(get_odd_doubled_numbers([]))
print(get_odd_doubled_numbers([1, 3, 5]))
print(get_odd_doubled_numbers([2, 4, 6]))

test_get_odd_doubled_numbers()