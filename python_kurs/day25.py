# """ООП Полиморфизм"""
# """
# Полиморфзм это одно и тоже имя функции (но разные сигнатуры)
# используется для разных типов.
# """
# def concat(a,b):
#     print(a+b)

# concat(5,8)                  #Ариф опер
# concat("web","developer")   #Kонкатенция





# # len
# #Встроеный полиморфные функци
# ls=[64123,543,5,36,234]
# str1="my book"


# #count
# ls2 = [45,3,34, 5,453,3,4,5,"python",True]
# str1 = "hello"
# print(str1.count("l"))


# ls4=[346, 54,34,5]
# ls4.pop()
# print(ls4)

# set1 = {45,3,34, 5,453,3,4,5,"python",True}
# set1.pop()
# print(set1)


#встроенный модуль math
# import day24
# from day24 import Zoo
# z = Zoo("Тигр","Бегемот","Жираф")
# print(z.aimal_1)
# from day24 import my_varible
# print(my_varible)
# import math
# from typing import Text
# print(math.pow(5, 3))
# print(5 ** 3)
# print(5 * 5 * 5)
# print(math.factorial(5))
# print(math.pi)


# radius = float(input("Введите раиус круга"))
# C = 2 * math.pi * radius
# print("Длина окружности равна:"+ str(C))
# print("Длина окружности равна:"C)


# radius = float(input("Введите площадь круга"))
# C = math.pi*math.pow(radius,2)
# print("Длина окружности равна:"+ str(C))
# print("Длина окружности равна:",C)

# P=float(input("Введите длину окружности:"))
# w=P/(2*math.pi)
# print("Радиус окружности равен:",w)

# print(math.sqrt(49))
# print(math.sqrt(4))
# print(math.sqrt(100))

# p = math.pi
# print(p)
# print(math.ceil(p))    #Округление в 
# print(math.floor(p))   #Округление в большую сторону



# """split(),loin()"""
# txt="python developer"
# print(len(txt))
# splitted = txt.split()
# print(len(splitted))
# print(splitted)


# txt2="python-developer"
# print(txt2.split("o"))
# ss = txt2.split("-")
# print(",".join(ss))



# """function open()"""
# #open (file_name, mode)
# mode-вид,режим
#MODE-режим
# r - Чтение - значение по умолчанию. Открывает файл для чтения,возвращает 
#ошибку если файл не существует 
# a - Добавить - 
# 
# 
# 
#
#
#
#
#
my_file=open("file.txt","r")
print(my_file)
print(my_file.read())
my_file.close()