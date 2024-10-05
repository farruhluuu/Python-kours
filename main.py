# my_list = [1, 5, 8, 11, 55, 62, 78, 86, 91]
# print(my_list[-1])

# old_list = [5, 6, 8, 99, 4, 62, 73]
# old_list.reverse()
# print(old_list)



# lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
# a = lst[0:33]
# b = lst[34:66]
# c = lst[67:100]
# a.append(b)
# b.append(c)
# print(a)

      # Ваша задача:
      # - разделите список на 3, заключите третий список внутрь второго, а второй внутрь первого [1...33,[34...66, [67..100]]]

#Problem4:
      # Напишите программу, которая удаляет последний элемент из массива: lst = [9, 5, 7, 4, 2, 6, 8, 1]


#Problem5:
      # Напишите программу, которая считает количество похожих элементов, в этом случае наш элемент "5" из массива: lst = [9, 5, 7, 5, 2, 6, 5, 1, 9, 54]


#Problem6:
      # Создать пустой лист. Добавить в него сначала ваше имя, год рождения, любимый язык программирования.


#Problem7:
      # Удалить из листа [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25] все чётные индексы до 10.
# lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
# lst.pop(1)
# lst.pop(3)
# lst.pop(5)
# lst.pop(7)
# lst.pop(9)

# print(lst)

# inp = input('Переводчик ')

# my_dict = {}
# my_dict['swim'] = "Плавать"
# my_dict['run'] = "Бегать"
# my_dict['jump'] = "Прыгать"
# my_dict['sleep'] = "Спать"
# my_dict['drink'] = "Пить"

# print(my_dict)

# fruits1 = { 'apple', 'cherry', 'banana', 'lemon', 'watermelon', 'coconut', 'salt' }
# fruits2 = { 'melon', 'potato', 'tomato', 'banana', 'carrot', 'lemon' }
# all=fruits1.intersection(fruits2)
# print(all)


# fruits1 = { 'apple', 'cherry', 'banana', 'lemon', 'watermelon', 'coconut', 'salt' }
# fruits2 = { 'melon', 'potato', 'tomato', 'banana', 'carrot', 'lemon' }
# print(a=fruits1.intersection_update(fruits2))


# fruits1 = { 'apple', 'cherry', 'banana', 'lemon', 'watermelon', 'coconut', 'salt' }
# fruits2 = { 'melon', 'potato', 'tomato', 'banana', 'carrot', 'lemon' }
# frut=fruits1.union(fruits2)
# print(frut)

# условия

# age = 15
# if  age < 18:
#       print("Не пить, не курить!")
# else:
#       print("welcome")



# print(sampleDict['class']['student']['marks']['history'])


# print(dict['b'] + dict['c'] + dict['d'][1] + dict['d'][3])


# Dict = {
#    'a':5,
#    'b':4,
#    'c':8,
#    'd':['good', 4, 7, 46]
# }
# b = []
# if Dict['a']%2 == 0:
#     b.append(Dict['a'])

# if Dict['b']%2 == 0:
#     b.append(Dict['b'])

# if Dict['c']%2 == 0:
#     b.append(Dict['c'])

# if Dict['d'][1] % 2 == 0:
#     b.append(Dict['d'][1])

# if Dict['d'][3] % 2 == 0:
#     b.append(Dict['d'][3])

# print(b[0] + b[1] + b[2] +b[3])


# menu={}
# menu = {
#    'Шашлык':80,
#    'Лагман':120, 
#    'Плов':200, 
#    'Десерты':{'Тирамису':150, 'Напoлеон':200, 'Три шоколада':250}, 
#    'Напитки' : {'Кок чай' : 20, 'Cola': 70}}


# menu['Пельмени'] = 160


# print(meny['шашлык'] * 4 + meny['десерты']['терамису'] * 6 + meny['пельмень'] + meny['напитки']['кок чай'] + meny['напитки']['cola'] * 1.5)

# print((menu["Шашлык"] * 4)+ menu["Пельмени"] + (menu["Десерты"]["Тирамису"] * 6) + menu["Десерты"]["Напoлеон"] + int(menu["Напитки"]["Кок чай"]) + int((menu["Напитки"]["Cola"] * 1.5)))



# accounts = {}
# accounts['cat@gmail.com'] = 'ko3a56ear3457sh73ka'
# accounts['run@gmail.com'] = 'b/e/246g26at'
# accounts['swim@gmail.com'] = 'p/lajhkjv/at'
# accounts['jump@gmail.com'] = 'pr234y234gat'
# accounts['sleep@gmail.com'] = 's23pa56234623t'
# acc = input('vvedite accaunt:')

# if acc in accounts:
#     print('tacoy acc est')
#     pin = input('vvedite parol: ')
#     if pin in accounts[acc]:
#         print('dobro pojalovat')
#     else:
#         print('ne verny parol')        
# else:
#     print('takoy acc ne sushestvuyet')


# print(sum(range(1,101))

# a = 1
# b = 2
# c = 3
# d = 4
# e = 5
# i = 1
# f = 6
# g = 7
# h = 8
# j = 9
# k = 10
# while i != 11:
#       if i == 1:      
#             print(a ,'*', i,'=', (a*i),'            ', b ,'*',i,'=', (b*i),'            ', c ,'*',i,'=', (c*i),'            ', d ,'*',i,'=', (d*i),'          ', e ,'*',i,'=', (e*i))
#       elif i == 2:
#             print(a ,'*', i,'=', (a*i),'            ', b ,'*',i,'=', (b*i),'            ', c ,'*',i,'=', (c*i),'            ', d ,'*',i,'=', (d*i),'          ', e ,'*',i,'=', (e*i))
#       elif i == 2 or i == 3:
#             print(a ,'*', i,'=', (a*i),'            ', b ,'*',i,'=', (b*i),'            ', c ,'*',i,'=', (c*i),'            ', d ,'*',i,'=', (d*i),'         ', e ,'*',i,'=', (e*i))
#       elif i == 10:
#             print(a ,'*', i,'=', (a*i),'          ', b ,'*',i,'=', (b*i),'          ', c ,'*',i,'=', (c*i),'          ', d ,'*',i,'=', (d*i),'        ', e ,'*',i,'=', (e*i))
#       elif i == 3 or i == 2 or i == 4:
#             print(a ,'*', i,'=', (a*i),'            ', b ,'*',i,'=', (b*i),'            ', c ,'*',i,'=', (c*i),'           ', d ,'*',i,'=', (d*i),'         ', e ,'*',i,'=', (e*i))
#       else:
#             print(a ,'*', i,'=', (a*i),'            ', b ,'*',i,'=', (b*i),'           ', c ,'*',i,'=', (c*i),'           ', d ,'*',i,'=', (d*i),'         ', e ,'*',i,'=', (e*i))
#       i += 1
# print(" ")
# i = 1
# while i != 11:
#       if i == 1:      
#             print(f ,'*', i,'=', (f*i),'            ', g ,'*',i,'=', (g*i),'            ', h ,'*',i,'=', (h*i),'            ', j ,'*',i,'=', (j*i),'          ', k ,'*',i,'=', (k*i))
#       elif i == 10:
#             print(f ,'*', i,'=', (f*i),'          ', g ,'*',i,'=', (g*i),'          ', h ,'*',i,'=', (h*i),'          ', j ,'*',i,'=', (j*i),'        ', k ,'*',i,'=', (k*i))
#       else:
#             print(f ,'*', i,'=', (f*i),'           ', g ,'*',i,'=', (g*i),'           ', h ,'*',i,'=', (h*i),'           ', j ,'*',i,'=', (j*i),'         ', k ,'*',i,'=', (k*i))
#       i += 1
      
# for e in __builtins__.__dict__: print(e)


# print("""      
# 1 * 1 = 1              2 * 1 = 2              3 * 1 = 3              4 * 1 = 4            5 * 1 = 5
# 1 * 2 = 2              2 * 2 = 4              3 * 2 = 6              4 * 2 = 8            5 * 2 = 10
# 1 * 3 = 3              2 * 3 = 6              3 * 3 = 9              4 * 3 = 12           5 * 3 = 15
# 1 * 4 = 4              2 * 4 = 8              3 * 4 = 12             4 * 4 = 16           5 * 4 = 20
# 1 * 5 = 5              2 * 5 = 10             3 * 5 = 15             4 * 5 = 20           5 * 5 = 25
# 1 * 6 = 6              2 * 6 = 12             3 * 6 = 18             4 * 6 = 24           5 * 6 = 30
# 1 * 7 = 7              2 * 7 = 14             3 * 7 = 21             4 * 7 = 28           5 * 7 = 35
# 1 * 8 = 8              2 * 8 = 16             3 * 8 = 24             4 * 8 = 32           5 * 8 = 40
# 1 * 9 = 9              2 * 9 = 18             3 * 9 = 27             4 * 9 = 36           5 * 9 = 45
# 1 * 10 = 10            2 * 10 = 20            3 * 10 = 30            4 * 10 = 40          5 * 10 = 50

# 6 * 1 = 6              7 * 1 = 7              8 * 1 = 8              9 * 1 = 9            10 * 1 = 10
# 6 * 2 = 12             7 * 2 = 14             8 * 2 = 16             9 * 2 = 18           10 * 2 = 20
# 6 * 3 = 18             7 * 3 = 21             8 * 3 = 24             9 * 3 = 27           10 * 3 = 30
# 6 * 4 = 24             7 * 4 = 28             8 * 4 = 32             9 * 4 = 36           10 * 4 = 40
# 6 * 5 = 30             7 * 5 = 35             8 * 5 = 40             9 * 5 = 45           10 * 5 = 50
# 6 * 6 = 36             7 * 6 = 42             8 * 6 = 48             9 * 6 = 54           10 * 6 = 60
# 6 * 7 = 42             7 * 7 = 49             8 * 7 = 56             9 * 7 = 63           10 * 7 = 70
# 6 * 8 = 48             7 * 8 = 56             8 * 8 = 64             9 * 8 = 72           10 * 8 = 80
# 6 * 9 = 54             7 * 9 = 63             8 * 9 = 72             9 * 9 = 81           10 * 9 = 90
# 6 * 10 = 60            7 * 10 = 70            8 * 10 = 80            9 * 10 = 90          10 * 10 = 100
# """)


# lst = [12,4,5,32,41,5,5,22,52,5]
# y = [i for i in lst]
# print(y)

# print("hello world\n"*10)

# from random import randint
# s=0
# n=int(input())
# for i in range(n):
#       a = randint(1,100)
#       s+=a
#       print(a,end=" ")
# print()
# print(s)

# for i in range(1,6):
#       print('*'*i)

# txt = 'dfhw77r89th7r8t79h9s8f76hs9th789'
# a = [ i for i in txt if i.isdigit()]
# print(a)

# for i in range(1,11):
#       print(2**i)

# r = [2,3,4,5,6,6,4,33,43,236,3,33,3,3,4,4,5,6,6,4,3,34,5,6,3,5,6,5,44,6,3,5,4,566,5,4,5,5]


      
# password = "8439527538"


# for i in range(3):
      # for j in range(5):
      #       print(i, end='')
      # print()
      
      
# summ = (lambda num1, num2: num1 + num2)(4,8)      
# print(summ)

# декараторы

# def add_functionality(func):
#       def inner():
#             print("I got decorared")
#             print(func().upper())
#       return inner()

# @add_functionality
# def ordinry():
#       return "I am ordinary"

# import datetime

# start = datetime.datetime.now()
# for i in range(100000000000):
#       ...
# print(i)
# print(datetime.datetime.now()-start)

# def time(func):
#       def t():
#             start = datetime.datetime.now()
#             print(func())
#             print(datetime.datetime.now()-start)
#       return t

# @time
# def clik():
#       for i in range(1000):
#             ...
#       return i

# clik()

# def apple(func):
#     def pear():
#         a = func()
#         b = 1
#         for i in range(1, a+1):
#             b *= i
#         return b
#     return pear



# @apple
# def orange():
#     a = 5
#     b = 10
#     return a+b

# print(orange())


# def decarator(func):
#       def inner():
#             print('start decarator...')
#             func()
#             print('finish decarator...')
#       return inner()

# def say():
#       i = 0
#       while True:
#             print(i)
#             i += 1
#             if i == 100:
#                   print("end")
#                   break

# d = decarator(say)

# d()

# t = decarator(say)

# elf = {
#       "health":50,
#       "speed":100
# }


# class Hello():
#       MAX_SPEED = 100
#       def __init__(self, race, damage=1):
#             self.race = race
#             self.damage = damage
# c = Hello('Elf')
# c.MAX_SPEED = 900
# print(c.MAX_SPEED)


# class Hello():
#       MAX_SPEED = 100
#       def __init__(self, race, damage=1):
#             self.damage = damage
#             self._race = 60
#             self.__race = race
#       def hit(self, damage):
#             self.__health = damage
# c = Hello('Elf')
# print(c._Hello__race)

# c._health = 5
# print(c._health)


# import cv2

# Включаем первую камеру
# cap = cv2.VideoCapture(0)

# "Прогреваем" камеру, чтобы снимок не был тёмным
# for i in range(30):
#     cap.read()

# Делаем снимок    
# ret, frame = cap.read()

# Записываем в файл
# cv2.imwrite('cam.png', frame)   

# Отключаем камеру
# cap.release()





# def num(a,b):
#       return a+b

# num(1,2)




# если НОД (a,b) = 1, то a и b - взаимнопростые числа

# a = int(input("Введи число: "))
# b = int(input("Введи число: "))
# while a != b:
#       if a > b:
#             a=a-b
#       else:
#             b=b-a
# print(a)


# a = int(input("Введи число: "))
# b = int(input("Введи число: "))
# while b > 0:
#       c = a % b
#       a = b
#       b = c
# print(a)


# a = 1.34*10000000000000000000000
# a = a * 25000
# print(a)