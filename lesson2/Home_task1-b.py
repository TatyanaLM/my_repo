var1 = int(input("Press first number "))
var2 = int(input("Press second number "))
var3 = int(input("Press third number "))

if var1 > var2 and var1 > var3:
    print("Max number ", var1)
elif var2 > var1 and var2 > var3:
    print('Max number ', var2)
else:
    print('Max number ', var3)

if var1 < var2 and var1 < var3:
    print("Min number ", var1)
elif var2 < var1 and var2 < var3:
    print('Min number ', var2)
else:
    print('Min number ', var3)

if var1 % 3 == 0 and var1 % 5 != 0:
    print(var1)
if var2 % 3 == 0 and var2 % 5 != 0:
    print(var2)
if var3 % 3 == 0 and var3 % 5 != 0:
    print(var3)