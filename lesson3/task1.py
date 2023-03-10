#task a
print('Задачка 1')
numbers = [1, 23, 56, 21, 56]
for i in range(len(numbers)):
    print(numbers[i]**2)

#task b
print('Задачка 2')
numbers = [45, 67, 34, 98, 12]
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        print(numbers[i])

print('Задачка 1 решение учителя')
numbers = [1, 23, 56, 21, 56]
for i in numbers:
    print(i ** 2)