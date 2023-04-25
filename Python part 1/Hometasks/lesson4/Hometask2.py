n = int(input("Введите размер вклада: "))
m = int(input("Введите срок вклада в годах: "))

def deposit (n, m):
    rate = 0.06
    for i in range(m):
      n = n + n * rate
    return n
if m == 1:
    print(f"Сумма вклада через {m} год составит {deposit(n, m)}")
elif 1 < m <= 4:
    print(f"Сумма вклада через {m} года составит {deposit(n, m)}")
else:
    print(f"Сумма вклада через {m} лет составит {deposit(n, m)}")
