list1 = [1,2,3]
list2 = [10,20,30]

#print(list(map(lambda x,y: x+y, list1, list2)))

#a = [1,2,3,4,5,6]

#print(list(filter(lambda x: x%2==0, a)))


dictionary = [{'name': "python", 'points': 10}, {'name': "java", 'points': 8}]
print(list(filter(lambda x:x['name'] =='python', dictionary)))

dictionary = [{'name': "python", 'points': 10}, {'name': "java", 'points': 8}]
print(list(filter(lambda x:x['name'] =='python', dictionary))[0]['points'])