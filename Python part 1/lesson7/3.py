#file_path =  указывать отдельно путь к файлу

f = open('ex.txt', 'r', encoding='utf8')
contents = f.read()
print(contents)
f.close()

with open('ex.txt', mode='w', encoding='utf8') as f:
    f.write('Новая строка 1\n')
    f.write('Новая строка 2\n')
    
with open('ex.txt', mode='a', encoding='utf8') as f:
    f.write('Новая строка 1\n')
    f.write('Новая строка 2\n')

with open('ex.txt', mode='r', encoding='utf8') as f:
    for line in f:
        print(line)