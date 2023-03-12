n = int(input("Введите размер вклада: "))
m = int(input("Введите срок вклада в годах: "))

def deposit (n, m):
    rate = 0.08
    for i in range(m):
      n = n + n * rate
    return n

print(f"Сумма вклада через {m} лет составит {deposit(n, m)}")