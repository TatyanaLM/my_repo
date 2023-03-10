numbers = input("press numbers ")
max = 0
min = 9
for i in numbers:
    num = int(i)
    if num > max:
        max = num
    if num < min:
        min = num
    if num % 3 == 0:
        if num % 5 != 0:
            print(i)
print('Максимальное число ', max)
print('Минимальное число ', min)