#Изучите функцию permutations из itertools.
# Напишите программу выводящую все возможные варианты для списка [1,2,3]

from itertools import permutations

x = [1, 2, 3]
print(list(permutations(x)))