
"""Задача: Написать программу, которая принимает на вход строку и возвращает список всех уникальных слов в этой строке.
При этом использовать только базовые операции, цикл for, функции и контейнерные типы данных."""


def unique_words(str):
    str_list = str.split()
    sings = ["?", ".", ",", "!", "-"]
    str_list = [current_word[:-1].lower() if current_word[-1] in sings else current_word.lower() for current_word in str_list]
    #print(str_list)
    result = []
    for current_word in str_list:
        if result.count(current_word) == 0:
            result.append(current_word)
    return result


assert unique_words("hello world") == ["hello", "world"]
assert unique_words("apple apple banana cherry") == ["apple", "banana", "cherry"]
assert unique_words("Python is great, isn't it?") == ["python", "is", "great", "isn't", "it"]
assert unique_words("hello world Hello World") == ["hello", "world"]
print(unique_words("hello world Hello World"))