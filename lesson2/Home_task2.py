numbers = input("press numbers ")
for i in numbers:
    num1 = int(i)
    m = 2
    for j in numbers:
        num2 = int(j)
        if num1 == num2:
            m = m - 1
    if m != 0:
        print("число", num1)

