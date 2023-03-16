
from Hometask1_lesson5.utils import calculate_change

price = float(input("Введите стоимость товара: "))
paid = input("Введите купюры внесенные в кассу: ")

change = calculate_change(price, paid)

#print(f'Сдача: {change}')
print(f'Купюры для сдачи: {change}')
#print(f'Количество купюр/монет: {change}')

