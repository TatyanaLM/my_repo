tallie = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
#написать функцию, которая переводит римское число в десятичные
def roman_to_decimal(roman_number):
    decimal_number = 0
    for i in range(len(roman_number)):
        if i > 0 and tallie[roman_number[i]] > tallie[roman_number[i - 1]]:
            decimal_number += tallie[roman_number[i]] - 2 * tallie[roman_number[i - 1]]
        else:
            decimal_number += tallie[roman_number[i]]
    return decimal_number


if __name__ == "__main__":
    roman_number = input("Введите римские цифры: ")
    print(roman_to_decimal(roman_number))