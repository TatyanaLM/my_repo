#def add(x,y):
    #return x+y
#print(add(2,3))

add = lambda x, y: x + y
print(add(3,3))

def multiply(z):
    return z*2

print(list(map(multiply, [1,2,3,4,5])))
#MAP(действие, итерируемый объект) действие применим на каждый его объект

print(list(map(lambda x: x*2, [1,2,3,4,5])))