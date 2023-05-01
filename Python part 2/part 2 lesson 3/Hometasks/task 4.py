"""Задача 4: Напишем рекурсивную функцию, которая вычисляет сумму цифр числа"""

def sum_of_digits(a):
    if a < 10:
        return a
    else:
        return a % 10 + sum_of_digits(a // 10)

#print(sum_of_digits(10455))
#print(sum_of_digits(1))
#print(sum_of_digits(999999999999999))
def test_sum_of_digits():
    assert sum_of_digits(0) == 0
    assert sum_of_digits(5) == 5
    assert sum_of_digits(10) == 1
    assert sum_of_digits(12345) == 15
    assert sum_of_digits(999999999999999) == 135
    print("All test_sum_of_digits pass")

test_sum_of_digits()

