# """dictionary-словарь-хеш таблица"""

# dct = dict({"ru":"Russian","kg":"Kyrgyzstan"})
# dct2 = {"en":"English", 5:"five", True:[545,87,False],"tuple": (54,8532)}
# print(dct2)
# print(len(dct2))
# print(dct2["tuple"])
# print(dct2["en"])
# print(dct2[True][1]+dct2[True][0])

# dct2[5] = "пять"     # изменить значение
# print(dct2)

# dct2[True][2] = 15
# print(dct2)

#print(dct2[True][1]+dct2[True][2]+dct2[True][0])
# dct2[True][1] = (dct2[True][1]+dct2[True][2]+dct2[True][0])
# print(dct2)

# del dct2["tuple"]    #удаление
# print(dct2)



# menu = {}
# menu ["beshbarmak"] = 130
# print(menu)
# menu ["lagman"] = 120
# print(menu)
# menu["lagman"] = 135
# print(menu)
# menu["borsh"] = 90
# print(menu)
# del menu["borsh"]
# print(menu)
# menu["drinks"] = ["Coca-cola", "Fanta", "Sprite"]
# print(menu)

# print("Сумма всех блюд",menu["beshbarmak"]+menu ["lagman"])
# print(menu)
# menu



# names = {}

# name = input('Input your name')
# profession = input("Input your profession")
# names ["name"]=name
# names ["profession"]=profession
# print(names)



# """Методы у обьекта класса <dict>: keys(), velues(), items()"""

# dct2 = {"en":"English", 5:"five", True:[545,87,False],"tuple": (54,8532)}

# dct2=(dct2.keys())  #вывести на терминал все ключи у словаря dct2  
# dct23=(dct2.values())     #вывести на терминал все значения у словаря dct2  
# dct23=(dct2.items())    #вывести на терминал все ключи и значения  у словаря dct2  
# print(dct23)

# problem 1
# обьедените словари 

# dct = {"ru":"Russian","kg":"Kyrgyzstan"}
# dct2 = {"en":"English", 5:"five", True:[545,87,False],"tuple": (54,8532)}

# problem 2
# Ниже представлены два списка . Напишите программу Python для преобразования их в словарь таким образом, чтобы элемент из списка 1 был ключом, а элемент из списка 2 - значением.

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

#Problem3 
#mat2 = [ 
#     [5, 6, 7, 8],
#     [9, 10, 11,12],
#     [13, 14, 15, 16],
#     [17, 18, 19, 25]
# ]   
# Найти сумму и количество всех чисел
# Количество: 16 

#Problem4

# 4. Создай программу которая проверяет сложность пароля:
# Если длина пароля:
#   меньше 4: <<очень легкий>>.
#   больше 4 и меньше 8: <<простой>>.
#   больше 8: <<надежный пароль>>.









mat2 = [ 
    [5, 6, 7, 8],
    [9, 10, 11,12],
    [13, 14, 15, 16],
    [17, 18, 19, 25]
]   
print(len(mat2[0]+mat2[1]+mat2[2]+mat2[3]))



















# numbers = {"Ten":10, "Twenty":20, "Thirty":30}
# print(numbers)




# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                  "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
# sampleDict=(sampleDict.values ["history"])
# print(sampleDict)
# dct2=(dct2.values())     
# #вывести на терминал все значения у словаря dct2  




# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}
# print(sample_dict.keys("name","age"))

# a = "apple and banana"
# print(a.startswith("p"))

# grocery = ('Milk, Chicken, Bread, Butter')
# # maxsplit: 2
# print(grocery)
# print(grocery.split(', ', 5))
# grocery.insert(1, 34)
# print(grocery)



# students = []
# a1 = input('Input your name')
# students.append(a1)
# a2=input('Input your name')
# students.append(a2)
# a3 = input('Input your name')
# students.append(a3)
# a4 = input('Input your name')
# students.append(a4)
# a5 = input('Input your name')
# students.append(a5)
# print(students)


# dct = {"name":"Alina", "age":15, "gender":"woman", "is_students":False, "colors":["black", "white", "yellow"]}
# print(dct["is_students"])
# # dct["Alina is favorite color"] = "yellow"
# # print(dct)
# dct["age"] = 20
# print(dct)
# del dct ["is_students"]
# print(dct)

# fd = {458:"True",45:78}
# sd = {"turn":"True","text":78}
# fd.update(sd)
# print(fd)
# print({**fd, **sd})




# d = {}
# d[keys[0]] 









# sampleDict = {
#      "class": {
#          "student": {
#              "name": "Mike",
#              "marks": {
#                   "physics": 70,
#                  "history": 80
#              }
#          }
#       }
# }

# # sampleDict["class":[10]]
# print(sampleDict["class"]['student']['marks']['history'])
# print(sampleDict["class"]['student']['name'])
# del sampleDict["class"]['student']['marks']["physics"]
# print(sampleDict)





# numbers ={}
# numbers[1] = 1**3
# numbers[2] = 2**3
# numbers[3] = 3**3
# numbers[4] = 4**3
# numbers[5] = 5**3
# numbers[6] = 6**3
# numbers[7] = 7**3
# numbers[8] = 8**3
# numbers[9] = 9**3
# numbers[10] = 10**3
# print(numbers)


# numbersOff = [548, -23, 34, -77, 0, 12, -5, 36, -34, -60, 3, -9]
# print(numbersOff[1]+numbersOff[3]+numbersOff[6]+numbersOff[8]+numbersOff[9]+numbersOff[11])


# lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25] 
# lst.pop(1)
# lst.pop(2)
# lst.pop(3)
# lst.pop(4)
# lst.pop(5)
# lst.pop(6)
# print(lst)

# dictionary_1 = {'a': 300, 'b': 400}
# dictionary_2 = {'c': 500, 'd': 600, 'qweg':1235}
# dictionary_1 = {'a': 300, 'b': 400, **dictionary_2}
# print(dictionary_1)







