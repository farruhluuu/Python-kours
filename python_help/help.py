# a=(str(input('input yourname;')))
# print(a.title())



# greg = "23" # string
# helo = 14 # integer
# print(type(helo))
# helo = "14"
# boolen = True # boolean
# flot = 4.6 # float
# print(boolen)
# print(greg+float)
# print(greg)
# print(type(helo))


# print(type(boolen))
# print(type(flot))
# one = [1, 9, 1]
# two = [1, 9]
# print(one != two)
# print(type(helo))
# print(type(a))
# 5
# print(a)
# # №2) Пользователь Вводит своё имя и Фамилию, вам надо вывести в терминал Приветственное письмо (Привет {Фамилия} {Имя}!)
# 



# b = 12
# a = 13
# print("привет", a, "hello", b )
# print(f"hello {a} hello  {b}")

# a = input("input your number:")
# print(a+5)
















# b=int(input("input your number"))
# c=int(input("input  your number:"))
# d=int(input("input  your number:"))

# print(b+c+d)
# print(b*c*d)
# print(d/a)
# print(a**a)

# print(b**b)
# print(c**c)
# print(d**d)

# a = input("Ваше имя:")
# b = int(input("Год рождение:"))
# print(f"Добро пожаловать!  {a} ")
# print(f"Вам {2021-b} лет")

# a=int(input("input  your number:"))
# b=int(input("input your number"))
# c=int(input("input  your number:"))
# d=int(input("input  your number:"))
# e=int(input("input  your number:"))

# print(c)

# print(5+74-53*3.14//6+54)

# 4 Problem
# Пользователь вводит два числовых значения
# Вам надо их сравнить и вывести: 
# а) Большее из них (True, False, False)
# б) Меньшее (False, True, False)
# в) Если же они равны, (False, False, True)






    
# a = int(input("Введите число:")) 
# b = int(input("Введите число:"))
# if a > b:
#     print('Большее число:', a)
# else: 
#     print('Большее число:', b)

# 5 Problem
# У вас есть два числа: 5 и 7
# Пользователь вводит знак (+, -, /, *), Вы должны совершить арифметическое вычесление, тоесть, если Ползователь ввёл "+", Вы должны вывести 5 + 7 в терминал и так далее.


# a = (input("Введите число:")
# b = input("Введите число:")
# if   a + b:   
#     print(a + b)
# elif a / b:
#     print(a/b)


# a = 5
# b = 7
# operation = input("арифметическая операция(+, -, /, *): ")

# if operation == "+":
#     print(a+b)



# age = int(input("Жаш: "))
# if age > 18 or age == 18 :
#     print("Толтурса болот!")
# elif age < 18:
#     print("Болбойт")
# else:
#     print("Туура сан жаз!")



    # haca1 = set(sequence_0)
# if len(sequence_0) == len(haca1):
#     print("1-Последовательность уникален")
# else:
#     print("1-Не уникален")
# haca2 = set(sequence_1)
# if len(sequence_1) == len(haca2):
#     print("2-Последовательность уникален")
# else:
#     print("2-Не уникален")

# haca3 = set(sequence_2)
# if len(sequence_2) == len(haca3):
#     print("3-Последовательность уникален")
# else:
#     print("3-Не уникален")


# haca4 = set(sequence_3)
# if len(sequence_3) == len(haca4):
#     print("4-Последовательность уникален")
# else:
#     print("4-Не уникален")





# сколько вам лет 12
# вы подросток
# вы взрослый
# ребенок 






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









# mat2 = [ 
#     [5, 6, 7, 8],
#     [9, 10, 11,12],
#     [13, 14, 15, 16],
#     [17, 18, 19, 25]
# ]   
# print(len(mat2[0]+mat2[1]+mat2[2]+mat2[3]))



# a = [1,2,3,4,5]
# a[0]= 4
# print(a)

# a = (1,2,3,4,5)
# print(a)

# lst = [1,2,3,4,5,6,7,8,9,10]
    #  0 1 2 3 4 5 6 7 8 9




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
#                  "



# def cal():
#     a = int(input())
#     b = input()
#     c = int(input())
#     if b == '+':
#         print(a+c)
#     elif b == '-':
#         print(a-c)
#     elif b == '*':
#         print(a*c)
#     elif b == '/':
#         print(a/c)
#     elif b == '%':
#         print(a%c)
#     elif b == '//':
#         print(a//c)
#     else:
#         print("Error")
        
# cal()


# print(chr(  ))
# print(ord('a'))

# value = 'cat-кот'
# repr(value)  # 'cat-кот'
# ascii(value)  # 'cat-\\u043a\\u043e\\u0442'


# name = 'Семен'
# mid_name = 'Семенович'
# balance = 32.56
# text = '''Дорогой {n} {m}, баланс вашего лицевого счета составляет {b} руб.'''.format(b=balance, m=mid_name, n=name)
# print(text)

# name = 'faruh'
# job = 'developer'
# language = 'Python C++'



# print(f''' 
# name: {name}     
# job: {job} 
# language {language}    
# ''')

# for i in range(1,11):
#     print(f'''{i}''', end='-')


# def sayHello():
#     print('he',end='')
#     print('ll',end='')
#     print('o',end='')
    
# sayHello()

# def sayHello():
#     print("hello world")
#     print("hello world")
#     print("hello world")

# sayHello()


# def multiply(b,c):
#     print(b+c)
# multiply(12,2)


# def even(a):
#     if a%2==0:
#         print(a,'четное')
#     else:
#         print(a,'нечетное')

# for i in range(10,21):
#     even(i)



# def factorial(n):
#     pr = 1
#     for i in range(2,n+1):
#         pr=pr+i
#     print(pr)
    
# factorial(4)    

# def fib(n):
#      a, b = 0, 1
#      while a < n:
#          print(a, end=' ')
#          a, b = b, a+b
#      print()
# fib(1000)


# def input_user():
#     a = input('')
#     print(a)
    
# input_user()

# def cikl(n):
#     i = 1
#     while i < n+1:
#         print(i)
#         i += 1
        
# cikl(100)

# def number():
#     a = int(input())
#     for i in range(a):
#         if i % 2 == 0:
#             print(i,"четное")
#         else:
#             print(i,"нечетное")
            
# number()


 

