var1 = int(input("Press first number "))
var2 = int(input("Press second number "))
var3 = int(input("Press third number "))
var4 = int(input("Press fourth number "))
var5 = int(input("Press fifth number "))

if var1 != var2 and var1 != var3 and var1 != var4 and var1 != var5:
    print("Number ", var1)
elif var2 != var1 and var2 != var3 and var2 != var4 and var2 != var5:
    print("Number ", var2)
elif var3 != var1 and var3 != var2 and var3 != var4 and var3 != var5:
    print("Number ", var3)
elif var4 != var1 and var4 != var2 and var4 != var3 and var4 != var5:
    print("Number ", var4)
else:
    print('Number ', var5)