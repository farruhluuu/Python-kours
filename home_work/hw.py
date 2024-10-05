# from day2_new import add


# add(2,5,4)









# Найти площадь треугольника
# import math 

# print("Длины сторон треугольника:")
# a = float(input("a = "))
# b = float(input("b = "))
# c = float(input("c = "))
# p = (a + b + c) / 2
# from math import sqrt
# s = sqrt(p * (p - a) * (p - b) * (p - c))
# print("Площадь: %.2f" % s)

# # Задание 2:


# Класс Alphabet
# 1. Создайте класс Alphabet
# 2. Создайте метод init(), внутри которого будут определены два динамических свойства: 1) lang - язык и 2) letters - список букв. Начальные значения свойств берутся из входных параметров метода.
# 3. Создайте метод print(), который выведет в консоль буквы алфавита
# 4. Создайте метод letters_num(), который вернет количество букв в алфавите
# class Alphabet:
#     def __init__(self ,lang,letters):
#         self.lan=lang
#         self.let=letters
#     def print(self):
#         print('алфавит',self.let)  
#     def letters_num(self):
#         print('количество',len(self.let))
# al=Alphabet("english",26)
# al.print()
# al.letters_num()
# Создайте класс Factory и внутри создайте 2 метода:
# a.Метод engine который возвращает строку "Двигатель создан"
# b.Метод bridge который возвращает строку "Ходовая часть создана"
# class Factory:


# # Задание 4:
    # Напишите программу, которая циклично запрашивает у пользователя любой символ
    # и выводит этот символ.
    # Завершает работу при вводе нуля.

# s =5
# a =(input("Введите любой символ:"))
# while True:
#     # a =(input("Введите любой символ:"))
#     if a==s: 
#         # break
#         print("Да,верно!!")
#         break
#     # a =(input("Введите любой символ:"))

# foo = {'Price':17,9:22,17:24,8:11}
# print(foo['Pricr'])
# print(‘’ 10 % 3)
# c = ([[1,2], [2,3], [4,5]])
# print(c[1])

# def func():


# 1 Создайте программу, которая будет вычислять возраст пользователя по его году рождения (2022 - год рождения).
# Если input = 1996, output = 26; Если input = 2003, output = 19
# string = 90
# string = int(string)
# print(string-3)


# num1 = int(input("1-число:"))
# num2 = int(input("2-число:"))
# print(num1-num2)

# 2 Создайте простейший калькулятор, пользователь вводит два числовых значения, вам надо вывести сумму, разность и первое число в степени второго числа.
# Если input = 2 и 3, output = 5, 0.6, 8; Если input = 4 и 2, output = 6, 2, 16
# num1 = int(input("1-число:"))
# num2 = int(input("2-число:"))
# print (num1+num2)
# print (num1-num2)
# print (num1 ** num2)

# 3 Веселитесь!