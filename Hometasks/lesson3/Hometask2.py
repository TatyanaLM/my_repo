numbers = input("Введите список чисел через пробел: ").split()
numbers.reverse()
result = []
for i in numbers:
    result.append(int(i))
print("Список в обратном порядке: ", result)