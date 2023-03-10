#словари ключ и значение
names_dict = {1:"Jan", 2:"Kevin", 3:"Mike"}
names_dict[4]="Kolenka"
print(names_dict.keys())
print(names_dict.values())
print(names_dict.items())
print(names_dict[1])

for k, v in names_dict.items():
    print(f"Key is {k}")
    print(f"Value for {k} is {v}")
