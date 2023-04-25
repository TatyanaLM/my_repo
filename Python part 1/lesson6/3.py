#
import random

roll_the_dice =  input("Нажмите y чтобы бросить кубики: ")

while roll_the_dice == 'y':
    x = random.randint(1, 6)
    y = random.randint(1, 6)
    print(x)
    print(y)
    roll_the_dice = input("Еще раз? ")
else:
    print("Жаль, что вы не хотите поиграть...")


print(random.uniform(0, 5.9))