#рекурсия
#факториал
#5! = 1*2*3*4*5

def fact(n):
    return 1 if n==0 else n* fact(n-1)
print(fact(5))

def append_default(element, lst =[]):
    lst.append(element)
    val = 50*2
    return lst, val
a, b = append_default("1")
print(a, b)
