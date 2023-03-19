words = input("Введите слова через запятую: ")
words_list = [word.strip() for word in words.split(",")]
words_list.sort()
print(words_list)
