# # Integer
# # String
# # Float
# # Boolean

# # переменный 

# # input

# ###### Операторы #######

# # +             Сложение
# # -             Вычитание
# # *             Умножение
# # /             Деление
# # //            Целочисленное деление
# # **            Возведение в степень
# # %             Деление по модулю
# # ==            Равно
# # < или >       Больше или Меньше
# # <=            Больше или равно
# # >=            Меньше или равно
# # !=            Не равно
# # print(2 * 2)




# # print


# ######################  Integer
# ######################  Float

# # print(12 + 12.5)
# # print(12 - 12.5)
# # print(-12 / 12.5)
# # print(12 * 12.5)
# # print(12  2)
# # print(12 // 5)
# # print(12 % 12.5)
# # print(12 = 12.5)
# # print(12 == 12.5)
# # print(12 <= 12.5)
# # print(12 >= 12.5)
# # print(12 < 12.5)
# # print(12 > 12.5)
# # print(12 != 12.5)



# ######################### String

# # print('xa' + ' ' + 'xa')
# # print('xa' + 'xa')
# # print('xa'*5)
# # print('xaxa' == 'xa'*2)  # True
# # print('xa'!='xa')        # False
# # print('xa'>'xa')         # False
# # print('xa'<'xa')         # False
# # print('xa'<='xa')        # True
# # print('xa'>='xa')        # True


# # capitalize
# # txt = "python is FUN!"

# # txt = input("Введите имя:")
# # x = txt.upper()
# # print(x)    

# # txt = "Welcome to my world"
# # x = txt.title()
# # print(x)                           # Welcome To My World

# # txt = "Hello my FRIENDS"
# # x = txt.lower()
# # print(x)                                  # hello my friends


# # txt = "Hello, welcome to my world."
# # x = txt.index("welcome")
# # print(x) 

# # txt = "Hello, welcome to my world."
# # x = txt.endswith(".")






# # """Нужно создать 4 переменных которые принимают имя, фамилия, возраст и пол"""

# # "Ответ: Иван Иванович 57 лет. Пол:Мужской"


# # inp = input("Введите ваше имя:").title()
# # inp2 = input("Введите ваше фамилия:").title()
# # inp3 = input("Введите ваш возраст:")
# # inp4 = input("Введите ваш пол:").title()
# # print(inp +inp2 + ' ' + inp3+ ' ' + inp4)

# # print(x)






# # txt = "Hello, welcome to my world."
# # x = txt.find("welcome")
# # print(x) 
 
# # txt = "987"
# # x = txt.isdigit()
# # print(x)

# # txt = "hgfkg"
# # x = txt.isalpha()
# # print(x)
# # txt = "aa12"
# # txt = "aa"
# # txt = " "
# # txt = "12"

# # x = txt.isidentifier()
# # print(x) 


# # txt = "Hello, And Welcome To My World!"
# # x = txt.istitle()
# # print(x)                               # True       

# # txt = "THIS IS NOW!"
# # x = txt.isupper()
# # print(x)                                  # True  


# # """Индекс"""
# #       #0\1\2\3\4
# # txt = "Hello, And c To My World!"
# # #                                         -3,-2,-1

# # # print(txt[2], txt[3])

# # print(txt[::3]) # пропускает по 3 значений
# # print(txt[3:]) # читает начиная с 3го
# # print(txt[::-1]) # читает наоборот
# # print(txt[4:7]) # читает диапазон












# # myTuple = ("John", "Peter", "Vicky")
# # x = "#".join(myTuple)                     
# # print(x)                                 # John#Peter#Vicky

# # txt = "Hello my FRIENDS"
# # x = txt.lower()
# # print(x)                                  # hello my friends


# txt = "welcome to the jungle"
# x = txt.split()
# print(x)                                  # ['welcome', 'to', 'the', 'jungle']


# # txt = "Hello My Name Is PETER"
# # x = txt.swapcase()
# # print(x)                       # hELLO mY nAME iS peter



# # #use a dictionary with ascii codes to replace 83 (S) with 80 (P):
# # mydict = {83:  80}
# # txt = "Hello Sam!"
# # print(txt.translate(mydict))        # Hello Pam!

# print(ord('+'))                     # 83
# print(ord('P'))                     # 80
# print(ord('R'))                     # 80
















"""for-while-цикл"""

# Цикл while используется в Python для неоднократного исполнения определенной инструкции до тех пор, пока заданное условие остается истинным. Этот цикл позволяет программе перебирать блок кода. Сначала программа оценивает условие цикла while. Если оно истинное, начинается цикл, и тело while исполняется.

# a = 1

# while a < 16:
#     print('Цикл выполнился', a, 'раз(а)')
#     a = a+0
# print('Цикл окончен')

# dct = 


# lst = [3, 2, 4, 'MADANA']
# for i in lst:
#     print("Значение 2: индекс 1")
# print(i)










# a = 0
# while a != 16:
#     print (' Цикл выполняется ', a, 'раз(а)')
#     # a += 2
# print ("cikl okonchen. "







# lst = [1, 2, 2, 3, 4, 6, 4, 7, 8, 9]

# for i in lst:
#     l = lst.index(i)
#     print (f'значение {i} индекс {l}')


# print (' varian 2')
    
# lst = [1, 2, 2, 3, 4, 6, 4, 7, 8, 9]  
# a = 0
# for i in lst:
#     print ('Znachenie', i, 'index', a)
#     a += 1




# lst = [1, 2, 2, 3, 4, 6, 4, 7, 8, 9]
# r = 0
# while r != len(lst):
#     print ('znachenie', lst[r], 'index', r)
    
#     r += 1

# lst = [1, 2, 2, 3, 4, 6, 4, 7, 8, 9]
# # 
# for l, i in enumerate(lst):
#     print (f'значение {i} индекс {l}')


# lst = [1, -2, 2, 3, -4, 6, -4, 7, 8, -9]

# for i in range(1, 15, 2):
#     print(i)









# numbers = [12, 45, 78, 52, 47] 
# for i in numbers: 
#     print(i)
# print(range(22)) 




















# for i in range (len(numbers)):  #1) i=0                               #1) i=1
#         print(numbers[i])       #print(numbers[0])= 12                 #print(numbers[1])= 45
#     1) i=2                       #1) i=3                             #1) i=4
#       print(numbers[2])= 78        #print(numbers[3])=52             #print(numbers[4])=47

# for i in numbers:
#     print(i)



# my_list = [54, 45, 1, 2,  8, 12]
# print(range)
# for i in my_list:
#     print(i)



# my_list=[15, 485, -8, 85, -15, -478, 231]
# for i in my_list:
#     if i % 5==0:
#         print(i)




# for i in range(11, 60, 2):
#     print(i)




# for i in range(11, 60, 2):
#     print(i)   #(11, 60, 2)
    # print(i)


# my_list=[15, 485, -8, 85, -15, -478, 231]
# for i in range(len(my_list)):
#     print("Индекс-",i,"число-",my_list[i])


# Используя for выведи на экран число от 10 до 100:


# for i in range(10, 100):
#      print(i)
     
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 66]
# for i in a:
#     # if isinstance(+)
#         print(i)



# for i in range(1, 100):
#   if i % 3==0:
#         print(i)




# 1. Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран; Например, 0+1+2+3+…+100
# i=0
# for a in range(101):
#     i += a 
# print(i)


# 2. Найти все число делящееся на 7 без остатка из ряда чисел от 7 до 457 и вывести на экран

# a=7
# while a < 457:
#     if a % 7 == 0:
#         print(a)
#     a+=1


# 3. Дан список(Lists): 
# numbersOff = [548, -23, 34, -77, 0, 12, -5, 36, -34, -60, 3, -9, -5667]
# Посчитать сумму только отрицательных чисел из списка numbersOff С ПОМОЩЬЮ ЦИКЛА

# a = 0
# for i in numbersOff:
#     if i<0:
#         a=a+i
# print(a)
# 4. Вывести на экран все чётные значения в диапазоне от 1 до 100;
# # 

# for i in range(0, 100, 2):
#     print(i)

# 5. Вывести на экран все нечётные значения в диапазоне от 1 до 100;

# for i in range(1, 100, 2):
#     print(i)

# 6. Записать в список(Lists) все числа в диапазоне от 10 до 2500;

# a = []
# for i in range(10, 2501):
#     a.append(i)
#     print(a)



# a=[]
# i=10
# while i<2501:
#     i=i+1
#     a.append(i)
# print(a)







# while True:
#     name = input('Type your name:')
#     print(name)
#     if name == 'Abdulhakim':
#         print(f'Hello {name}')
#         break





# while True:
#     name = input('Type your name:')
#     print(name)
#     if name == 'Zarina':
#         continue
#     print('Hello')

import random

# Используя for выведи на экран число от 10 до 100:






# Напишите алгоритм где можно угадывать диапазон цифр и пока не угадаешь ту цифру он должен работать  бесконечно

# С помощью random()
# random_number = random.randint(12, 50)
# print(random_number)


# random1=random.randint(1,30)
# print(random1)
# while True:
#     random2=int(input('Type your dijit:'))
#     if random1==random2:
#         print('Suprize')
#         break



#Создай программу которая проверяет сложность пароля бесконечно пока пользователь не ввел надежный пороль

# Если длина пароля:
#   меньше 4: <<очень легкий>>.
#   больше 4 и меньше 8: <<простой>>.
#   больше 8: <<надежный пароль>>.


# while True:
    # pw = input("Придумайте пароль: ")
    # dig = pw.isdigit()
    # alp = pw.isalpha()
    # if len(pw) < 8:
    #     print ("Придумайте пароль сложнее!")
    #     continue
    # elif len(pw) >= 8:
    #     if dig == True:
    #         print ("Добавте буквы!")
    #     elif alp == True:
    #         print ("Добавьте цифры!")
    #     else:
    #         print ("Пароль принят!! ")
    #         break
    #         continue







# Напишите алгоритм который выводит количевство и сумму и все элементы по 1
# my_lst =[1, 2, 3, 4]

# Output:
# 1
# 2
# 3
# 4
# Сумма: 10
# Количевство: 4













# gg = input("Введите пороль:")
# pasword ="qwerty0987"
# while gg!=pasword:
#     print("Введите правильно")
#     gg=input("Введите пороль:")














# i = 0
# my_lst =[1, 2, 3, 4]
# while i < len(my_lst):
#     print(my_lst[i])
#     i =i + 1
# my_lst = [1, 2, 3, 4]
# i = 0
# sum1 = 0
# col = 0
# while i < len(my_lst):
#     sum1 = sum1 + my_lst[i]
#     col =col + 1
#     i = i + 1
# print("Сумма:",sum1)
# print("Количевство:",col )






# random_number = random.randint(4,34)
# print(random_number)
# while True:
#     inp = int(input())
#     if inp == random_number:
#         break








# """Двухмерные массивы """


# my_list2= [
#   [45,78,45,12],
#   [5, 787, 78, 15],
#   [8, 2, 45, 877]
# ] 

# n= []
# for i  in my_list2:
#     n.extend(i)
# print(sum(n), len(n))



#  Выведите сумму и количество всех чисел в переменной my_list2 





# my_list3 =   [[45,-78,-45,12],
#             [5, -787, 78, 15],
#             [8, 2, 45, 877]]
# my_list3 =   [[45,-78,-45,12],
#             [5, -787, 78, 15],
#             [8, 2, 45, 877]]
# lst = []
# t = []

# for i in my_list3:
#     lst.extend(i)

# for q in lst:
#     if q < 0:
#         t.append(q)
                            
# print ('kolvo', len(t))
# print ('Summa', sum(t))

# l = []
# for y in my_list3:
#     for u in y:
#         if u < 0:
#             l.append(u)
# print ('Summa:', sum(l), '\ncollich:', len(l))





# Високосный год делится без остатка на 4, за исключением столетий (года заканчивающиеся на 00). Столетние года, мы будем делить  на 400, если делится без остатка, то этот год является високосным. При делении как и в предыдущем примере, мы будем использовать оператор %.





# 1. С помощью while у человека имя фамилию и отчество:
# Проси до тех пор пока человек не вводит свои данные
# while True:
#     name = input("")
#     name2 = input("")
#     name3 = input("")
#     if name == 'Ivan' and name2=='Ivanov' and name3=='Ivanovich':
#         print('Welcome')
#         break

# 2. Дан список гостей, на сегодняшную вечеринку :
# guests = ['Axe', 'Tom', 'Jax', 'Rik', 'Sam', 'Zot']
# Создай цикл while чтобы проверить приходящих гостей.
# Если человек вводит имя которое нет в списке то выводи
#   Сообщение: Извините, ваше имя нет списке. Sorry.
# Если человек вводит имя которое есть в списке то выводи
#   Сообщение: Добро пожаловать гость заходите и наслаждайтесь.

# while True:
#   guests = ['Axe', 'Tom', 'Jax', 'Rik', 'Sam', 'Zot']
#   a=input("Type your name here:")
#   if a in guests:
#     print('Добро пожаловать гость заходите и наслаждайтесь.')
#     break
#   else:
#     print('Извините, ваше имя нет списке. Sorry.')












# """Тернарный оператор"""


# x = 253
# y = 50
# v = 965

# x= 253
# y = 505
# v = 96
# big = (x if x>v else v) if x>y else (y if y > v else v)
# print(big)



# a=5
# b=8
# c=3
# s = (a if a > c else c) if a > b else (b if b > c else c)
# print(s)





"""Генераторы списков | List comprehensions"""

# lst = [1,2,3,4,5,5,4,3,2,1]
# n = [i for i in lst if i < 3]
# print(n)





# lst = [5, 8 ,7, 12, 56, 87, 55, 10, 4, 3,]
# lst2 = []
# for i in lst:
#     if i>5:                                       #Цикл по элементу
#         lst2.append(i)
# print(lst2)
    
lst = [5, 8 ,7, 12, 56, 87, 55, 10, 4, 3, 4]
# lst3 = [i for i in lst if i > 5]
# print(lst3)



array = [21, 32, 4]
# Напишите алгоритм который проверяет все ли элементы одинаковы, если все одинаковы то в терминал должен выводить: "Все элементы уникальны". Иначе: "Есть одинаковые числа"


# setarr = set(array)
# if len(array) == len(setarr): 
#     print("Все элементы уникальны")
# else:
#     print("Есть одинаковые числа")

# r = ('Уникальные' if len(set(lst)) == len(lst) else 'Не уникальные')
# print(r)






# txt = 'dfhw77r89th7r8t79h9s8f76hs9th789'
# Выделите цифры в новый лист



















# Именные функции, инструкция def
# Функция в python - объект, принимающий аргументы и возвращающий значение. Обычно функция определяется с помощью инструкции def.

# def add(z):
#     summ = 0
#     for i in z:
#         if i<0:
#             summ=summ+i
#     print(summ)
#     # print(z)
# counter = 0
# o = 'k'
# for i in r:
#     counter = counter +1
# print(counter)

r = [4,5,834,3,73,358, -77, -3]
def length(znachenie):
    counter = 0
    for i in znachenie:
        counter = counter +1
    return  counter


# lenn = length(r)
# print(lenn)

# def minn(array):
#     array_d = {}.fromkeys(array, 0)
#     for a in array:
#         array_d[a] += 1
#     print(array_d)

# minn([24,6,2456,734,2,6,54,4,4654,45])


# lst = [12,23,23,65,63,89,54,56]
# st = {}
# for i in lst:
#     l = 0
#     for j in lst:
#         if i == j:
#             l += 1 
#     st[i] = l
# for i in st:
#     print(f'{i: <7} {st[i]}')


# ls = [2, 1, 2, 2, 3, 4, 4, 3, 5, 5 ,6, 8, 9, 8, 1, 1]
# def contr(value):  
#     st = {}
#     for i in ls:
#         p = 0
#         for e in ls:
#             if i == e:
#                 p += 1
#         if p > 1:
#             st[i] = p
            
#     for c , v in st.items():
#         print(f"Znachenie {c} - {v} raza povtoryaetcya" )

# contr(ls)

# import random 


# st = ['Чынгыз ака', 'Бектур ака', 'Азиз ака', 'Фаиз ака', 'Кудурет ака', 'Мадина', 'Гулжигит']

# print(random.choices(st, k=4))


# r = [84,63,80,47]
# g = 0
# for i in r: 
#     g+=i
# print(g/4)

# r = ''' '''

# h = ''
# for i in r:
#     if i.isdigit() or i == ':' or i ==  '-' or  i == '>' or i == '<' or i ==  ',':
#         i == ''
#     else:
#         h += i
# print(h)

 

# """ *args **kwargs"""

# def fun(*args, **kwargs):
#     print(kwargs)
# pet=[1,2,3,4,5,6]
# fun(2,3,4,2,4,5,7,pet)



# import time
# def func_running_time(func):
#     def fn():
#         start = time.time()
#         f = func()
#         print(time.time()-start)
#         return f
#     return fn


# @func_running_time
# def add():
#     x = [4,5,834,3,73,358, -77, -3]
#     summ = 0
#     for i in x:
#         summ=summ+i
#     print(summ)
#     print(summ)
# add()




# import time

# def function_running_time(func):
#     def fun(*args,**kwargs):
#         start = time.time()
#         result = func(*args,**kwargs)
#         print(time.time()-start)
#         return result
#     return fun

# @function_running_time
# def add(z):
#     summ = 0
#     for i in z:
#         summ=summ+i
#     print(summ)


# add([4,5,834,3,73,358, -77, -3])
# my_list2= [[45,78,45,12],
#             [5, 787, 78, 15],
#             [8, 2, 45, 877]]
# print(length(my_list2))





# pas = int(input('''
# Введите номер карты:

# >>>'''))
# balance = 10000
# while pas != True:
#     if pas == 1234:
#         n = int(input('''
# 1 - Если хотите вывести деньги введите 1:
# 2 - Если хотите пополнить баланс нажмите 2:
# 3 - Если хотите узнать курс валюты нажмите 3:
# 4 - Если хотите узнать баланс нажмите 4:
# 0 - Для завершение программы нажмите на 0:

# >>>'''))
#         if n == 1:
#             num1 = int(input('''
# Какую сумму хотите вывести?

# >>>'''))
#             if num1 < balance :
#                 balance -= num1
#                 print('Ваш баланс:', balance, 'cом')
#             elif num1 > balance:
#                 print('''
# Недостаточно средств.
# ''')
#         elif n == 2:
#             num2 = int(input('''
# Насколько вы хотите пополнить счёт?

# >>>'''))
#             if num2 <= 10000 or num2 >= 10000:
#                 balance += num2
#                 print('Ваш баланс:', balance, 'cом')
#         elif n == 3:
#             print('''USD - 84.01
# EUR - 87.16
# RUB - 1.374
# KZT - 0.1179
# CNY - 10.50
# GBR - 0.00
# ''')
#         elif n == 4:
#             print('Ваш баланс:', balance, 'cом')
#         elif n == 0:
#             break
#     else:
#         pas = int(input('''
# Введите номер карты:

# >>>'''))





# Напишите функцию,которая принимает два аргумента a и b,и цикл должен “пробежаться” по цифрам от a до b и записать числа, которые делятся на 3 без остатка в список three, 
# а числа, которые делятся на 5 без остатков в список five. Числа, которые делятся без остатков как на 3, так и на 5, запишите в список three_five. Используйте деление по модулю.(%)


# Напишите функцию, которая берет "a (int)" и *args (int). Ваша задача найти сумму всех четных чисел в *args и вычитать "a" 


# Напишите функция для бота, которая принимает параметр hours и умеет здороваться утром и днём, но ей нужно добавить приветствия для ночи и вечера. Напишите условную конструкцию,
#  которая выводит уместные сообщения:

# ВРЕМЯ ТЕКСТ ПРИВЕТСТВИЯ
# до 6  Доброй ночи!
# до 12 Доброе утро!
# до 18 Добрый день!
# до 23 Добрый вечер!
# в остальных случаях   Доброй ночи!

# Подсказка
# Создайте конструкцию if-elif-else с тремя elif и логическим оператором <.
# Ключевые слова elif и else должны располагаться точно под if
# После условий в elif и после ключевого слова else нужны двоеточия.
# Блоки кода под elif и else должны отбиваться четырьмя пробелами.


# Написать Функцию которая принимает предложение как аргумент, считает
# количество букв и возвращает сколько символов он ввёл. НЕ ИСПОЛЬЗОВАТЬ
# функцию len()

# def length(st):
#     counter=0
#     for i in st:
#         counter += 1
#     return counter
# cc = input()

# print(length(cc))



# Использование **kwargs для передачи аргументов ключевого слова переменной функции

# вывод будет:
# имя - Джон
# фамилия - Вуд
# Возраст - 22
# Телефон - 1234567890

# def ben(**kwargs):
#     print(kwargs)
# ben(name='Джон', surname='Wood', age=22, phone=99655555555)


# """
#     1. выясните процентное соотношение мужского пола и женского.
#     2. выведите имена всех студентов с курса python
#     3. уберите дубликаты
#     4. выведите студентов, которые старше 30 и найдите процент их количества относительно других
#     5. все студенты курса javascript перешли на курс python. Как вы поменяете это в словаре ? Напишите код

# """

# students = [ 
#     {'name': 'Mark', 'age': 18, 'course': 'java', 'gender': 'Male'}, 
#     {'name': 'John', 'age': 15, 'course': 'python', 'gender': 'Male'}, 
#     {'name': 'Andrew', 'age': 20, 'course': 'javascript', 'gender': 'Male'}, 
#     {'name': 'Marcus', 'age': 25, 'course': 'java', 'gender': 'Male'}, 
#     {'name': 'Agnes', 'age': 40, 'course': 'python', 'gender': 'Female'}, 
#     {'name': 'Doe', 'age': 42, 'course': 'java', 'gender': 'Male'}, 
#     {'name': 'Michael', 'age': 17, 'course': 'javascript', 'gender': 'Male'}, 
#     {'name': 'Jennifer', 'age': 16, 'course': 'java', 'gender': 'Female'}, 
#     {'name': 'Angela', 'age': 16, 'course': 'python', 'gender': 'Female'}, 
#     {'name': 'Eniston', 'age': 34, 'course': 'java', 'gender': 'Male'}, 
#     {'name': 'Albert', 'age': 33, 'course': 'javascript', 'gender': 'Male'}, 
#     {'name': 'Nash', 'age': 28, 'course': 'python', 'gender': 'Male'}, 
#     {'name': 'Nicolas', 'age': 19, 'course': 'java', 'gender': 'Male'}, 
#     {'name': 'Alex', 'age': 21, 'course': 'java', 'gender': 'Male'}, 
#     {'name': 'Martin', 'age': 22, 'course': 'python', 'gender': 'Male'}, 
#     {'name': 'Gloria', 'age': 23, 'course': 'java', 'gender': 'Female'}, 
#     {'name': 'Mikkel', 'age': 24, 'course': 'python', 'gender': 'Male'}, 
#     {'name': 'Susann', 'age': 25, 'course': 'javascript', 'gender': 'Female'}, 
#     {'name': 'Steve', 'age': 26, 'course': 'python', 'gender': 'Male'}, 
#     {'name': 'Mark', 'age': 18, 'course': 'java', 'gender': 'Male'}, 
#     {'name': 'Johnathan', 'age': 15, 'course': 'python', 'gender': 'Male'}, 
#     {'name': 'Aidin', 'age': 20, 'course': 'javascript', 'gender': 'Male'},
#     {'name': 'Mirbek', 'age': 25, 'course': 'java', 'gender': 'Male'}, 
#     {'name': 'Aidana', 'age': 40, 'course': 'python', 'gender': 'Female'}, 
#     {'name': 'Atay', 'age': 42, 'course': 'java', 'gender': 'Male'}, 
#     {'name': 'Chyngyz', 'age': 17, 'course': 'javascript', 'gender': 'Male'}, 
#     {'name': 'Aigerim', 'age': 16, 'course': 'java', 'gender': 'Female'}, 
#     {'name': 'Jyldyz', 'age': 16, 'course': 'python', 'gender': 'Female'}, 
#     {'name': 'Emir', 'age': 34, 'course': 'java', 'gender': 'Male'}, 
#     {'name': 'Emirlan', 'age': 12, 'course': 'javascript', 'gender': 'Male'}, 
#     {'name': 'Nursultan', 'age': 13, 'course': 'python', 'gender': 'Male'}, 
#     {'name': 'Aliaskar', 'age': 19, 'course': 'java', 'gender': 'Male'}, 
#     {'name': 'Aktan', 'age': 21, 'course': 'java', 'gender': 'Male'}, 
#     {'name': 'Adyl', 'age': 14, 'course': 'python', 'gender': 'Male'}, 
#     {'name': 'Gloria', 'age': 23, 'course': 'java', 'gender': 'Female'}, 
#     {'name': 'Janyl', 'age': 16, 'course': 'python', 'gender': 'Female'}, 
#     {'name': 'Meerim', 'age': 12, 'course': 'javascript', 'gender': 'Female'}, 
#     {'name': 'Sultan', 'age': 13, 'course': 'python', 'gender': 'Male'}, ]






# import time


# def func_running_time(func):
#     def fn(*args):
#         start = time.time()
#         f = func(*args)
#         print(time.time()-start)
#     return fn


# @func_running_time
# def contr():  
#     st = {}
#     ls = [2, 1, 2, 2, 3, 4, 4, 3, 5, 5 ,6, 8, 9, 8, 1, 1]
#     for i in ls:
#         p = 0
#         for e in ls:
#             if i == e:
#                 p += 1
#         if p > 1:
#             st[i] = p
            
#     for c , v in st.items():
#         print(f"Znachenie {c} - {v} raza povtoryaetcya" )

# contr()




# numbers = [2,31,23,42,1,1]
# print(type(numbers))




# Problem1
# Напишите функцию, которая принимает любой тип формата файла с  расширением, вам нужно найти расширение у файла.
# Пример:

# Вход: music.mp3
# Вывод: расширение mp3


    # Ввод: image.png
    # Вывод: png

    # Ввод: file
    # Вывод: Расширение не найдено

# Ввод: problem.py
# Вывод: расширение py

# Ввод:  image.png
# Вывод: расширение png


# Ввод:: video.mp4
# Вывод: расширение mp4
# types_of_files = ['mp4', 'mp4', 'mp4', 'mp4', 'mp4']
# inp = input('Введите файл:')
# def den(a):
#     if '.' in a:

#         b = str(a).split('.')
#         print(f'Расширение у этого файла {b[-1]}')
#     else:
#         print('Расширение не найдено')
# den(inp)

# Problem2
# Напишите функцию, которая принимает число "а", вам нужно вывести звездочки от 1 до "а", как показано на результате
# а = 3
# * 
# **
# ***

# a = int(input('Введите число:'))
# def asterx(a):
#     while a != 0:
#         print('12 ' * a)
#         a -= 1
# asterx(a)

# s = int(input("type: "))

# def star(b):
#     a = 0 
#     while a < b:
#         a+=1
#         print(f'{a} ' * a)
# star(s)
# Problem3
# Напишите функцию, которая принимает число "n", вам нужно вывести цифры от 1 до "n", как показано на результате
# n = 4

# 1
# 2 2
# 3 3 3
# 4 4 4 4 

# Problem4
# l = ['Adam', 'Sultan', 'Anna']
# new_l = []
# в new_l записывать имена, которые начинаются с буквы A. Здесь нужно использовать list comprehensions

# l = ['Adam', 'Sultan', 'Anna']
# new_l = [i for i in l if i[0]=='A' or i[0]=='a']
# print(new_l)





"""  Классы   """

# class Hello():
#     def __init__(self, race=7, damage=1, armor=1):
#         self.race = race
#         self.damage = damage
#         self.armor = armor

# hello = Hello()
# print(hello.race)


# class Character():
#     max_speed = 100           #атрибут на уровне класса
#     dead_health = 0           #
#     def __init__(self, race = 'Krasavchik', damage =10, armor = 20):      #конструктор
#         self.race = race
#         self.damage = damage       # обычная переменная
#         self.armor = armor         #
#         self.health = 100
#     def hit(self,damage):       #метод - это функция внутри класса      
#         if self.armor < damage:
#             self.health += self.armor
#             self.health -= damage
#             self.armor = 0
            
#         else:
#             self.health -= (damage/2)
#             self.armor -= (damage/2)
   
#     def is_dead(self):
#         if self.health == Character.dead_health:
#             return "umer"
#         else:
#             return f'gotov k boyu. Zdorovie {self.health}% '

# azat = Character()
# # u = Character()              #экземпляр
# # e = int(input("Uron:"))
# # u.hit(e)
# # print('Zdorove', u.health)
# # print('Zashita', u.armor)
# # print(u.is_dead())

# print(azat.race)











"""   Константы | Защищённые и приватные атрибуты | Свойства   """


# self в конструкторе это как ссылка откуда мы  получаем атрибуты/переменные

# """ Константы """
# class Hello():
#     MAX_SPEED = 100  #  Это константа обычный атрибут на уровне класса изменение которых рассматриваемой программой не предполагается или запрещается 

#     def __init__(self, race, damage=1):      # конструктор класса python
#         self.race = race
#         self.damage = damage

# c = Hello('Elf')   # c - Экземпляр/Инстанция класса
# c.MAX_SPEED = 900 # но как видим в пайтоне мы можем его изменить
# print(c.MAX_SPEED)




# """ Защищённые и приватные атрибуты """

# class Hello:
#     MAX_SPEED = 100  #  Это константа обычный атрибут на уровне класса изменение которых рассматриваемой программой не предполагается или запрещается 

#     def __init__(self, race, damage=1):    # конструктор класса python
#         self.damage = damage # Обычный, публичный атрибут
#         self._healt = 60 # Защищенный атрибут
#         self.__race = race # Приватный атрибут

#     def hit(self, damage):
#         self._healt -= damage


# c = Hello('Elf')    #c - Экземпляр/Инстанция класса
# print(c._Hello__race)

# c._health = 5
# print(c._health)

# # Если вы хотите чтобы атрибут не был виден нигде то "__", а если хотите чтобы он был виден в наследниках то "_"


""" Свойства """

# class Hello():
#     MAX_SPEED = 100

#     def __init__(self, race, damage=1):    # конструктор класса python
#         self.damage = damage # Обычный, публичный атрибут   
#         self._healt = 60 # Защищенный атрибут     protected
#         self._current_speed = 100 # Защищенный атрибут   protected
#         self.__race = race # Приватный атрибут   privat

#     def hit(self, damage):
#         self._healt -= damage

#     @property   #С помощью декоратора "property" мы можем приватные и защищенные атрибуты сделать читаемым вне класса
#     def health(self):
#         return self._healt

#     @property
#     def race(self):
#         return self.__race

#     @property
#     def current_speed(self):
#         return self._current_speed

    
#     @current_speed.setter     # С помощью название атрибута .setter приватные и защищенные атрибуты можно сделать изменяемым
#     def current_speed(self, current_speed):
#         self._current_speed = current_speed

# # c = Hello('Elf')    c - Экземпляр класса
# c = Hello('Elf')
# c.current_speed = 150
# print(c.current_speed)

    





# "------ @classmethod ------"

# class User:

#     def __init__(self, name, email):
#         self.name = name
#         self.email = email

#     def get_info(self):
#         print(f'{self.name} - {self.email}')

#     @classmethod
#     def get_info_class(cls, ls=[1,2]):
#         a, b = ls
#         print(f'{a} - {b}')

# lst = ['Erlan', 'erlan@gmail.com']
# user = User
# user = user.get_info_class()



# """-----Наследование и полиморфизм-----"""

# ">>> Наследование <<<"

# class Shape():

#     def __init__(self):
#         print('Shape created')

#     def draw(self):
#         print('Drawing a shape')

#     def area(self):
#         return 'Calc area'


#     def perimetr(self):
#         print('Calc perimetr')

# # shape = Shape()


# class Rectangle(Shape):   # Дочерный класс или же наследник

#     def __init__(self, width, heigth):

#         Shape.__init__(self)

#         self.width = width
#         self.heigth = heigth

#         print('Rectangle created')

#     def draw(self):
#         print('Drawing a rectangle')

#     def area(self):  # Переопределение  метода базового класса
#         return self.width * self.heigth
    
#     def perimetr(self):   # Переопределение  метода базового класса
#         return 2 * (self.width + self.heigth)

# rect = Rectangle(5,5)
# # rect.draw()

# class Triangle(Shape):   # Дочерный класс или же наследник

#     def __init__(self, a, b, c):
#         # Shape.__init__(self)
#         self.a = a
#         self.b = b
#         self.c = c
        
#     # def area(self):  # Переопределение  метода базового класса
#     #     return self.a * self.a
    
#     def perimetr(self):   # Переопределение  метода базового класса
#         return self.a + self.b + self.c

# tri = Triangle(5,5,5)
# print(tri.area())



# # ">>> Полиморфизм <<<"

# # for shape in [rect, tri]:
# #     print(shape.perimetr())
 


# ">>> Множественное наследование <<<"
# class Cls(Rectangle, Triangle):
#     def __init__(self, width, heigth):
#         self.width = width
#         self.heigth = heigth

# cls = Cls(7,7)
# print(cls.area())



# class Vehicle:
#     def __init__(self, year, color, category):
#         self.year = year
#         self.color = color
#         self.category = category
         
# class Car(Vehicle):
#     def __init__(self, year, color, category, model):
#         super().__init__(year, color, category)
#         self.model = model

        


# Создайте базовый класс FlourProducts с аргументами wheat flour, eggs, oil, salt, water. И создайте дочерние классы Cake, Samsa и приготовьте всё это с помощью методов



        
        # # ">>> Инкапсуляция <<<"

# class Boyler:
    
#     def turn_on():
#         Boyler.__light()
#         print('Gotovo')
    
#     def __light():
#         print('in proces')
 
# boyler = Boyler
# boyler.turn_on()
# boyler._Boyler__light()



# import time 
# import asyncio

# async def w(number = 10000):
#     start = time.time()
#     v = 0
#     for i in range(number):
#         v+=i
#         o = 0
#         while o != number:
#             o += 1
#     print(v)
#     await asyncio.sleep(1)
#     print(time.time()- start)
# w()

# async def async_func(task_no):
#     print(f'{task_no} :Velotio ...')
#     print(f'{task_no}... Blog!')

# async def w(number = 1000):
#     v = 0
#     for i in range(number):
#         v+=i
#     print('Hello')
\



####################################
# Создайте класс Soda (для определения типа газированной воды), принимающий 1 аргумент при инициализации (отвечающий за добавку к выбираемому лимонаду). 
# В этом классе реализуйте метод show_my_drink(), выводящий на печать «Газировка и {ДОБАВКА}» в случае наличия добавки, а иначе отобразится следующая фраза: «Обычная газировка».

# class Soda():
#     def __init__(self, name):
#         self.name = name

#     def show_my_drink(self):
#         a = input('Хотите добавить вкус?: ')
#         if a == 'да':
#             c = input('Какой вкус вы желаете добавить?: ')
#             print(self.name + ' + ' + c +'ый вкус')
#         else:
#             print(self.name)

# b = Soda('Обычная газировка')
# b.show_my_drink()



# class Soda:
#     def __init__(self, dobavka):
#         self.dobavka = dobavka

#     def show_my_drink(self):
#         if self.dobavka != '':
#             print('Газировка и',self.dobavka)
#         else:
#             print('Обычная газировка')


# s = Soda('Лимон')
# s.show_my_drink()

# class Soda():
#     def __init__(self, water):
#         self.water = water
#     def show_my_drink(self, water):
#         if water > '':
#             print(f'Газировка и {water}')
#         else:
#             print('Обычная газировка') 

# water=input('Выбирите напиток:')
# a=Soda(water)
# a.show_my_drink(water)

# class Soda:
#     def __init__(self, sirop = 'обычная'):
#         self.sirop = sirop
    
#     def shov_my_drink(self):
#         return f'Газировка {self.sirop}'
# soda = Soda()
# print(soda.shov_my_drink())

####################################
# Создайте класс ПЕРСОНА с методами, позволяющими вывести на экран информацию о персоне, а также определить ее возраст (в текущем году). Создайте дочерние классы: АБИТУРИЕНТ (фамилия, дата рождения, факультет), СТУДЕНТ (фамилия, дата рождения, факультет, курс), ПРЕПОДАВАТЕЛЬ (фамилия, дата рождения, факультет, должность, стаж), со своими методами вывода информации на экран и определения возраста
# В родительском классе Persona() определим, в соответствии с условием задачи, метод vozrast(), служащий для определения возраста и метод info(), позволяющий вывести информацию о персоне. Далее создаем три дочерних класса: Abiturient(Persona), Student(Persona), Prepodavatel(Persona), основанные на классе Persona(). Соответственно, все дочерние классы будут наследовать методы родительского класса.

# class Persona():
#     def __init__(self, name, age, faculty):
#         self.name = name
#         self.age = age
#         self.faculty = faculty

# class Abiturient(Persona):
#     def __init__(self, name, age, faculty, info):
#         super().__init__(name, age, faculty)
#         self.info = info 
#         info = self.name, 2022 - age, faculty

# class Student(Persona):
#     def __init__(self, name, age, faculty, course, info):
#         super().__init__(name, age, faculty)
#         self.course = course
#         self.info = info 
#         info = (self.name, 2022 - age, faculty, course)

# class Propod(Persona):
#     def __init__(self, name, age, faculty, dol, staj, info):
#         super().__init__(name, age, faculty)
#         self.dol = dol
#         self.staj = staj
#         self.info = info
#         info = (self.name, 2022 - age, faculty, dol, staj)

# a = Abiturient('Бородин Александр Сергеевич', 2005, 'ТОР','Бородин Александр Сергеевич, 1992 года рождения, Факультет: ТОР')
# b = Student('Шайбеков Кудурет Медетбекович', 1998, 'Факультет: ГЭМ', '3 курс', 'Шайбеков Кудурет Медетбекович, 1998 года рождения, Факультет: ГЭМ, 3 курс')
# c = Propod('Варламов Дьулус Маркович',1976,'ГЭМ','Преподователь','3 года', 'Варламов Дьулус Маркович, 1976 года рождения, Факультет: ГЭМ, Должность: Преподователь, Стаж работы: 3 года')
# # print(a.name)
# # print(b.course)
# # print(c.age)

# while True:    
#     k = input('Информацию о ком хотите узнать?: ').title()
#     if k == 'Абитуриент' :
#         print(a.info)
#         continue
#     elif k =='Студент':
#         print(b.info)
#         continue
#     else:
#         print(c.info)
#         break
 


# class Persona:
#     def __init__(self, imya = 0, god_rojdeniya = 0, fakultet = 0):
#         self.imya = imya
#         self.god_rojdeniya = god_rojdeniya
#         self.fakultet = fakultet
#     def vozrast(self):
#         self.god_rojdeniya = 2022 - int(self.god_rojdeniya)
#         return self.god_rojdeniya 
    

#     def info(self):
#         return f'{self.imya, self.god_rojdeniya, self.fakultet}'
# persona = Persona('Oleg', 1900, 'MGU')        
# class Abiturient(Persona):
#     def __init__(self, imya, god_rojdeniya, fakultet):
#         super().__init__(imya, god_rojdeniya, fakultet)
        
#     def info(self):
#             return self.imya, self.god_rojdeniya, self.fakultet
# abiturient = Abiturient('Ivan', 1996, 'Econom')

# class Student(Persona):
#     def __init__(self, imya, god_rojdeniya, fakultet, kurs):
#         super().__init__(imya, god_rojdeniya, fakultet)
#         self.kurs = kurs

#     def info(self):
#         return self.imya, self.god_rojdeniya, self.fakultet, self.kurs

# student = Student('Thor', 1994, 'IT', 3)

# class Prepodavatel(Persona):
#     def __init__(self, imya, god_rojdeniya, fakultet,doljnost, staj):
#         super().__init__(imya, god_rojdeniya, fakultet)
#         self.doljnost = doljnost
#         self.staj = staj

#     def info(self):
#         return self.imya, self.god_rojdeniya, self.fakultet, self.doljnost, self.staj

# prepod = Prepodavatel('Vasiliy', 1989, 'muzic', 'teacher', '10let')

# print(student.vozrast())
# print(prepod.vozrast())
# print(abiturient.vozrast())
# print(prepod.info()) 
# print(abiturient.info())






# Ключевое слово повышения Python используется для возбуждения исключений или ошибок . Ключевое слово повышения вызывает ошибку и останавливает поток управления программой. Он используется для вызова текущего исключения в обработчике исключений, чтобы его можно было обработать дальше по стеку вызовов







"""СУБД (Cистема управления базами данных)  |  DBMS (database management system)"""


# СУБД – это система управления базами данных.


# СУБД отвечает за: поддержку языка Бд, механизмы хранения и извлечения данных и оптимизацию процессов извлечения данных итд


# SQL  -  Structured  Query  Language (Язык структруированных запросов)


# PostgreSQL — свободная объектно-реляционная система управления базами данных.



# Результирующий набоp - результат запроса SQL


# И записи называются кортежами


# SQL не процедурный язык, то есть в нем нельзя писать циклы итд



# DDL (Data Definition Language) - Create, Alter, Drop

# DML (Data Manipulation Language) - SELECT, INSERT, DELETE, UPDATE

# TCL (Transaction Control Language) - COMMIT, ROLLBACK, SAVEPOINT

# DCL (Data Control Language) - GRANT, REVOKE, DENY

# ANSI SQL-92

# PL/pgSQL — процедурное расширение/диалект языка SQL, используемое в СУБД PostgreSQL. 
# PL/SQL — процедурное расширение/диалект языка SQL, используемое в СУБД Oracle. 
# T-SQL — процедурное расширение/диалект языка SQL, используемое в СУБД MS/SQL. 



# Почему мы будем учить/использовать PostgreSQL?
# 1: Бесплатный
# 2: Инсталляция (установка и настройка Бд)
# 3: Мощность
# 4: Отвечает на все современные стандарты




"""  Установка | Installation  """
# Создаем репозиторий
# sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

# Импортируем репозиторий
# wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

# Обновляем пакеты
# sudo apt-get update

# Устанавливаем postgresql
# sudo apt-get -y install postgresql
























"""Типы данных в PostgreSQL"""

# Есть 6 основных типа данных 


# Integeral numbers (Целлые числа)
# smallint: весит 2 байт и в него входит 16 степень 2 от -32768 до 32768
# integer: весит 4 байт и в него входит 32 степень 2 от какого-то до какого-то
# bigint: весит 8 байт и в него входит 64 степень 2 от какого-то до какого-то


# Real numbers / Float numbers (Вещественные числа)
# numeric/decimal:Число с остатками, то есть не целлое число точный тип данных подходит для денежных математических вычислениях и не точно сколько он весит.
# real/float4 : Не целлое число, тип данных который подходит для научных вычислений весит 4 байт и поддерживает до 6 знаков после запятой
# float8: Не целлое число, тип данных весит 8 байт и поддерживает до 15ти знаков после запятой


# Integeral numbers (Целлые числа)
# smallserial: весит 2 байт от 1 до 32767
# serial: весит 4 байт от 1 до какого-то
# bigserial: весит 8 байт от 1 до какого-то


#  Characters (Символы)

# char: Здесь мы задаем сколько знаков\символов он должен принимать, если символов больше чем мы задали он не примет и если там меньше чем мы задали остальное место заполнит по умолчанию пробелами. Не точно сколько весит, зависит от кодировки

# varchar: Здесь мы задаем сколько знаков\символов он должен принимать, если символов больше чем мы задали он не примет и если там меньше чем мы задали остальное место уберет. Не точно сколько весит и так же это зависит от кодировки

# text: просто как str


# Logical

# Bool/Boolean: Весит 1 байт, он так же принимает 'y', '1', 'yes' ввиде True, 'n', '0', 'no' ввиде False



# Temporal (временной)

# time: Весит 8 байт и принимает время, 24 часа
# date: Весит 4 байт и хранит только даты, диапазон от 4713 год (Юлиа́нская да́та)
# timeshtamp: хранит и дату и время так же весит 8 байт
# interval: выведет разницу между двумя timeshtampами, до милисекунд. Весит 16 байт
# timeshtamptz: Хранит timezone и timeshtamp. Весит так же 8 байт


#  Другие типы данных

#  Arrays (массивы)
#  JSON
#  custom тип данных который мы сами можем создать
#  XML
#  NULL это ничто, не ноль, не пробел а НИ-ЧЕ-ГО


# Реализуйте родительский класс Publication, конструктор которого принимает name, date, pages, library, type
# Создайте субкласс Book. В конструктор родительского класса должен передавать type=’book’
# Создайте субкласс Magazine. В конструктор родительского класса должен передавать type=’magazine’
# Создайте субкласс Newspaper. В конструктор родительского класса должен передавать type=’newspaper’




# 1. Создайте класс Factory и внутри создайте 2 метода:

# a. Метод engine который возвращает строку "Двигатель создан"
# b. Метод bridge который возвращает строку "Ходовая часть создана"

# 2. Создайте класс Toyota который будет НАСЛЕДОВАТЬ класс Factory. В классе
# Toyota создайте методы wheels и windows.

# a. Метод wheels возвращает строку "Колёса готовы"
# b. Метод windows возвращает строку "Стёкла готовы"

# Из класса Toyota вызовите все методы, методы вернут вам строки(объекты)
# class Factory:
#     def engine(self):
#         return 'Двигатель создан'
#     def bridge(self):
#         return "Ходовая часть создана"

# class Toyota(Factory):
#     def wheels(self):
#         return "Колёса готовы"
#     def windows(self):
#         return "Стёкла готовы"
# factory = Factory()
# toyota = Toyota()
# print(toyota.engine(), toyota.bridge(), toyota.wheels(), toyota.windows())





################################################

# Создайте класс Person, у которого есть:

# конструктор init, принимающий 3 аргумента: name, surname, gender. Атрибут gender может принимать только 2 значения: "male" и "female", по умолчанию "male". Если в атрибут gender передается любое другое значение, печатать сообщение: 
# "Не знаю, что вы имели ввиду? Пусть это будет мальчик!" и проставить атрибут gender значением "male"
# переопределить метод str следующим образом: 
# если объект - мужчина (атрибут gender = "male"), возвращать строку "Гражданин <Фамилия> <Имя>
# если объект - женщина (атрибут gender = "female"), возвращать строку "Гражданка <Фамилия> <Имя>
# class Person:
#     def __init__(self, name, surname, gender = 'male'):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
        
#     def star(self):
#         if self.gender == 'male':
#             return f'Гражданин {self.name, self.surname}'
#         elif self.gender == 'female':
#             return f'Гражданка {self.name, self.surname}'
#         else:
#             self.gender = 'male'
#             return "Не знаю, что вы имели ввиду? Пусть это будет мальчик!", self.gender

# person = Person('ivan', 'ivanov', 'M')
# print(person.star())




################################################

# 1) Создать класс Phone, у него должен быть атрибут batteryLife, изначальное значение которого равно 100% и метод turnOn(), который при вызове понижает процент заряда телефона на 10%, также должен быть метод charge(), при вызове которого заряд повышается на 10%, но главное, нельзя чтобы он заряжал его больше чем на 100%.
# class Phone:
#     def __init__(self, batteryLife = 100):
#         self.batteryLife = batteryLife
#     def turnon(self):
#         if self.batteryLife == 0:
#             return 'Зарядки нет. 0%'
#         self.batteryLife -= 10
#         return self.batteryLife 
        
#     def charge(self):
#         if self.batteryLife < 100:
#             self.batteryLife += 10
#             return self.batteryLife
#         elif self.batteryLife >= 100:
#             return 'Зарядка 100%'
# phone = Phone()
# print(phone.charge())
# print(phone.turnon())
# print(phone.charge())



################################################
# Создать класс Salary. У него должно сеттер и геттер методы. Сеттер принимает 2 аргументa name, salary. В геттер должен вывести "<name> зарабатывает в месяц <salary>"
# Создать метод сountofYear, который посчитает сколько зарабатывает в год
#  <name> зарабатывает в год <salary>"
# class Salary:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#     def getter(self):
#         return f'{self.name} зарабатывает в месяц {self.salary} сом.'
#     def counToYear(self):
#         self.salary *= 12
#         return f'{self.name} зарабатывает в год {self.salary} сом.'

# salary = Salary('Ivan', 20000)
# print(salary.getter())
# print(salary.counToYear())




# class Factory():
#     def __init__(self,engine,bridge):
#         self.engine=engine
#         self.bridge=bridge
#     def En(engine):
#         print('engine created')
#     def Br(bridge):
#         print("Ходовая часть создана")
# class Toyota(Factory):
#     def __init__(self, engine, bridge,wheels,windows):
#         self.wheels=wheels
#         self.windows=windows
#         super().__init__(engine, bridge)
#     def Wh(wheels):
#         print("Колёса готовы")
#     def Win(windows):
#         print("Стёкла готовы")

# f=Factory('engine','bridge')
# f.En()
# f.Br()
# n=Toyota('engine','bridge','wheels','windows')
# n.Wh()
# n.Win()

# Реализуйте родительский класс Publication, конструктор которого принимает name, date, pages, library, type
# Создайте субкласс Book. В конструктор родительского класса должен передавать type=’book’
# Создайте субкласс Magazine. В конструктор родительского класса должен передавать type=’magazine’
# Создайте субкласс Newspaper. В конструктор родительского класса должен передавать type=’newspaper’

# class Publication():
#     def __init__(self,name, date, pages, library, type):
#         self.name = name
#         self.date = date
#         self.pages = pages
#         self.library = library
#         self.type = type
# class Book(Publication):
#     def __init__(self,name, date, pages, library, type):
#         self.name = name
#         self.date = date
#         self.pages = pages
#         self.library = library
#         self.type = 'Book'
#     def type_book(self):
#         print(self.name, self.pages )
# class Magazine(Publication):
#     def type_magazine(self):
#         print(self.name, self.pages )
# class Newspaper():
#     pass

# pt = Publication('Python', 2020, '300', 'pip', 'book')
# bt = Book()
# bt.type_book()

# 1. Создайте класс Factory и внутри создайте 2 метода:

# a. Метод engine который возвращает строку "Двигатель создан"
# b. Метод bridge который возвращает строку "Ходовая часть создана"
# class Factory():
#     def __init__(self, engine, bridge, wheels, windows):
#         self.engine=engine
#         self.bridge=bridge
#         self.wheels=wheels
#         self.windows=windows
#     def engine_1(self):
#         print(self.engine)
#     def bridge_1(self):
#         print(self.bridge)
# pr=Factory("Двигатель создан", "Ходовая часть создана", "Колёса готовы", "Стёкла готовы" )
# pr.engine_1()
# pr.bridge_1()

# 2. Создайте класс Toyota который будет НАСЛЕДОВАТЬ класс Factory. В классе
# Toyota создайте методы wheels и windows.

# a. Метод wheels возвращает строку "Колёса готовы"
# b. Метод windows возвращает строку "Стёкла готовы"

# Из класса Toyota вызовите все методы, методы вернут вам строки(объекты)

# class Toyota(Factory):
#     def wheels_1(self):
#         print(self.wheels)
#     def windows_1(self):
#         print(self.windows)
# pt=Toyota("Двигатель создан", "Ходовая часть создана", "Колёса готовы", "Стёкла готовы")
# pt.wheels_1()
# pt.windows_1()

################################################

# Создайте класс Person, у которого есть:

# конструктор init, принимающий 3 аргумента: name, surname, gender. Атрибут gender может принимать только 2 значения: "male" и "female", по умолчанию "male". Если в атрибут gender передается любое другое значение, печатать сообщение: "Не знаю, что вы имели ввиду? Пусть это будет мальчик!" и проставить атрибут gender значением "male"
# переопределить метод str следующим образом: 
# если объект - мужчина (атрибут gender = "male"), возвращать строку "Гражданин <Фамилия> <Имя>
# если объект - женщина (атрибут gender = "female"), возвращать строку "Гражданка <Фамилия> <Имя>
# class Person():
#     def __init__(self, name, surname, gender = 'male'):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
        
#     def star(self):
#         if self.gender == 'male':
#             return f'Гражданин {self.name, self.surname}'
#         elif self.gender == 'female':
#             return f'Гражданка {self.name, self.surname}'
#         else:
#             self.gender = 'male'
#             return "Не знаю, что вы имели ввиду? Пусть это будет мальчик!", self.gender

# person = Person('ivan', 'ivanov', 'female')
# print(person.star())


################################################

# 1) Создать класс Phone, у него должен быть атрибут batteryLife, изначальное значение которого равно 100% и метод turnOn(), который при вызове понижает процент заряда телефона на 10%, также должен быть метод charge(), при вызове которого заряд повышается на 10%, но главное, нельзя чтобы он заряжал его больше чем на 100%.
# class Phone():
#     def __init__(self, batteryLife = 100):
#         self.batteryLife = batteryLife
#     def turnon(self):
#         if self.batteryLife == 0:
#             return 'Зарядки нет. 0%'
#         self.batteryLife -= 10
#         return self.batteryLife 
        
#     def charge(self):
#         if self.batteryLife < 100:
#             self.batteryLife += 10
#             return self.batteryLife
#         elif self.batteryLife >= 100:
#             return 'Зарядка 100%'
# phone = Phone()
# print(phone.charge())
# print(phone.turnon())
# print(phone.charge())




################################################
# Создать класс Salary. У него должно сеттер и геттер методы. Сеттер принимает 2 аргументa name, salary. В геттер должен вывести "<name> зарабатывает в месяц <salary>"
# Создать метод сountofYear, который посчитает сколько зарабатывает в год
#  <name> зарабатывает в год <salary>
# class Salary:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#     def getter(self):
#         return f'{self.name} зарабатывает в месяц {self.salary} сом.'
#     def counToYear(self):
#         self.salary *= 12
#         return f'{self.name} зарабатывает в год {self.salary} сом.'

# salary = Salary('Ivan', 20000)
# print(salary.getter())
# print(salary.counToYear())



# Наконец-то Создание БД 

# Cоздание таблицы

# Для создания базы данных используется команда CREATE DATABASE , после которой указывается название базы данных.

# CREATE TABLE <название таблицы>          
#     (
#       <Название столбца> <тип данных> |здесь можно добавить "NOT NULL" чтобы поле был обязательным
#     );

# "CREATE TABLE" и все команды необязательно с "CAPSLK" но рекомендуется писать с "CAPSLK"


# CREATE TABLE publisher
# (
#   publisher_id integer PRIMARY KEY,
#   org_name varchar(130) NOT NULL, 
#   address text NOT NULL, 
# );


# CREATE TABLE book
# (
#   book_id integer PRIMARY KEY,
#   title varchar(200) NOT NULL, 
#   isbn varchar(13) NOT NULL, 
# );


# INSERT INTO book VALUES (id, 'Название', isbn)
# INSERT INTO publisher VALUES (id, 'Название организации/издателя', 'address')




# С помощью этой команды вы можете вывести данные какой то таблицы

# SELECT * FROM book



# Добавить столбец

# ALTER TABLE <название_таблицы>  ADD COLUMN <тип данных>;

# Удалить столбец

# ALTER TABLE <название_таблицы> DROP COLUMN <тип данных>;


# DROP TABLE book; удалить таблицу

# CREATE TABLE book
# (
#   book_id integer PRIMARY KEY,
#   title varchar(200) NOT NULL, 
#   isbn varchar(13) NOT NULL, 
#   fk_publisher_id integer REFERENCES publisher(publisher_id) NOT NULL
# );
