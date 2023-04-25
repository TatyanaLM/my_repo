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
    sum = 0
    for i in range(len(roman_number)-1):
        left = roman_number[i]
        print(left)
        right = roman_number[i+1]
        print(right)
        if tallie[left] < tallie[right]:
            sum -= tallie[left]
            print(sum)
        else:
            sum += tallie[left]
            print(sum)
    sum += tallie[roman_number[-1]]
    print(sum)
    return sum


if __name__ == "__main__":
    roman_number = input("Введите римские цифры: ")
    print(roman_to_decimal(roman_number))