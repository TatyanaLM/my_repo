#1. Напишите программу, принимающую на вход слова через запятую и выводящую слова в алфавитном порядке.
# Используйте List comprehension.

words = input("Введите слова через запятую: ")
words_list = [word.strip() for word in words.split(",")]
words_list.sort()
print(words_list)
