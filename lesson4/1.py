#a,b,c = 1,2,3
#print(a)
# зип перемешивает типы данных
print(list(zip([0,1,2], [4,5,6], [7,8,9])))
print(list(zip([0,1,2], "XYZ", [7,8,9])))
zip_list = list(zip([0,1,2], "XYZ", ["seven", "eight", "nine"]))
print(zip_list)

zip_list_2 = list(zip([0,1,2], "XYZ", {0: 'zero', 1:'one', 2:'two'}.values()))
print(zip_list_2)

list_of_numberss = [0,1,2]
string = "XYZ"
dictionary = {0: 'zero', 1:'one', 2:'two'}
dictionary = dictionary.values()
result_list = list(zip(list_of_numberss, string, dictionary))
print(result_list)