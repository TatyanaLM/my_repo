first_number = -100
last_number = -6
step = 1
min = first_number
max = last_number - 1
for i in range(first_number, last_number, step):
    if i % 3 == 0:
        if i % 5 != 0:
            print(i)
print('Максимальное число ', max)
print('Минимальное число ', min)