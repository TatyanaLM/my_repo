
"""Задача: Написать программу, которая принимает на вход список строк и возвращает новый список, содержащий только те строки, которые начинаются с большой буквы.
При этом использовать только базовые операции, цикл for, функции и контейнерные типы данных."""


def filter_capitalized_words(lst):
    result = []
    for str in lst:
        if str[0] == str[0].upper():
            result.append(str)
    return result

#print(filter_capitalized_words(["Python", "java", "C++"]))

assert filter_capitalized_words(["Apple", "Banana", "cherry"]) == ["Apple", "Banana"]
assert filter_capitalized_words(["Python", "java", "C++"]) == ["Python", "C++"]
assert filter_capitalized_words(["Red", "green", "Blue"]) == ["Red", "Blue"]