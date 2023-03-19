nominal = {5000, 1000, 500, 100, 50, 10, 5, 2, 1, 0.50, 0.10, 0.05, 0.01}
nominal = sorted(nominal, reverse=1)
def calculate_change(price, paid):
    price = float(price) # превращаю значение price в float
    list_paid = paid.split(" ") # разделяю значение paid по пробелу
    float_list_paid = [float(j) for j in list_paid] # делаю из разделенных значений список
    full_paid = sum(float_list_paid) # считаю сумму сколько покупатель внес, сумма элементов из списка
    if full_paid < price:
        raise ValueError("Дано мало денег")
    elif full_paid == price:
        return "Сдача не требуется"
    change = full_paid - price # считаю разницу между внесенным и стоимостью товара
    print(f'Сдача: {change}')
    result = [] #  создаю новый список, куда запишу купюры
    for i in nominal:
        if change // i > 0:
            diff = change // i
            for o in range(int(diff)):
                result.append(i)
            change = change - diff * i
    result = " ".join([str(a) for a in result])
    return result

if __name__ == "__main__":
    price = input("Введите стоимость товара: ")
    paid = input("Введите купюры внесенные в кассу: ")
    value = calculate_change(price, paid)
    print(f'Купюры для выдачи сдачи: {value}')