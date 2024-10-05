# """open()"""
# new_file = open("notebook.txt","w")
# new_file.write("Диагональ/разрешение 15.6/1366x768 пикс.Процессор\nIntel Core i5 Intel Core i5 2450M 2.5 ГГцОперативная память (RAM),4ГБ\nГрафический контроллер	Radeon HD 6370M \n1ГБОбъем HDD,0 ТБx750 ГБ")
# new_file.close()

# my_file2 = open("notebook.txt","r")
# # print(my_file2.read())
# my_notebook = my_file2.read()
# print(len(my_notebook))


# import math

# from day24 import lang_list
# print(lang_list)
# print(len(lang_list))

# count_letter=0
# for i in lang_list:
#     count_letter=count_letter+len(i)
# print(count_letter)
# # print(f"{count_letter} в факториале {math.factorial(count_letter)}")

# """open"""
# #r
# #w
# #a
# #x


# #создать файл
# # my_file = open("my_file.txt","x")

# #записать файл
# my_file2= open("my_file.txt", "w")
# my_file2.write("Hello world!!!\n")
# my_file2.close()

# #Добавить запись в конце
# my_file3 = open("my_file.txt", "a")
# my_file3.write("Hello everybody")
# my_file3.close



# my_file4= open("my_file.txt","a")
# my_file4.write("Python\n")
# my_file4.close()


# my_file5= open("my_file.txt","r")
# print(my_file5.read())

# my_file6=open("my_file.txt","a+")
# my_file6.write("New words")
# my_file6.read()
# my_file6.close()

# my_file5 = open("my_file.txt","r")
# # for i in my_file5:
# #     print(i,"good")

# m = my_file5.readlines()
# print(m)
# print(type(m))
# c = 0
# for i in m:
#     for letter in i:
#         if letter.lower() == "o":
#             c += 1
# print("o:",c)
# c = 0
# for i in m:
#     for letter in i:
#         if letter.lower() == "e":
#             c += 1
# print("e:",c)
# c = 0
# for i in m:
#     for letter in i:
#         if letter.lower() == "w":
#             c += 1
# print("w:",c)
# c = 0
# for i in m:
#     for letter in i:
#         if letter.lower() == "l":
#             c += 1
# print("l:",c)
# c = 0
# for i in m:
#     for letter in i:
#         if letter.lower() == "h":
#             c += 1
# print("h:",c)


# file_name=input("Напишите название файла для создания:")
# new = open(file_name, "x")

#Исключение
# file_name=input("Напишите название файла для создания:")
# try:
#     new = open(file_name, "x")
#     print("Файл создан")

# except FileExistsError:
#     print("Такой файл уже создана")



# a = int(input("Ведите 1-число:"))
# b = int(input("Ведите 2-число:"))
# try:
#     print("Результат: ", a / b)
# except ZeroDivisionError:
#     print("На ноль делить нельзя!!!")



# o = open("new_file","w")
# o.write("Всем привет!!!\n")
# o.write("Всем привет!!!")
# o.close()

# o2 = open("new_file","r")
# # print(o2.readlines())
# # print(o2.readline())
# print(o2.read(5))
# import os
# u=int(input("Для создания введите 1:\nДля записи введите 2:\nДля чтение введите 3:\nДля добавление введите 4:\nДля добавления и чтения введите 5:\nДля удаления файла введите 6:\nЕсли хотите создать папку введите 7:\nЕсли хотите удалить папку введите 8:"))
# if u == 1:
#     file_name=input("Напишите название файла для создания:")
#     try:
#         new = open(file_name, "x")
#         print("Файл создан")
#     except FileExistsError:
#         print("Такой файл уже создана")
# elif u == 2:
#     try:
#         p=input("Напишите название файла для записи:")
#         f=input("Что хотите:")
#         my_file2= open(f"{p}", "w")
#         my_file2.write(f"{f}\n")
#         my_file2.close()
#     except FileNotFoundError:
#         print("Такого файла не существует")
# elif u == 3:
#     e=input("Напишите название файла для записи:")
#     my_file5= open(f"{e}","r")
#     print(my_file5.read())

# elif u == 4:
#     try:
#         t=input("Напишите название файла для записи:")
#         o=input("Что хотите:")
#         my_file3 = open(f"{t}", "a")
#         my_file3.write(f"{o}")
#         my_file3.close
#     except FileNotFoundError:
#         print("Такого файла не существует")
# elif u == 5:
#     try:
#         x=input("Напишите название файла для записи:")
#         d=input("Что хотите:")
#         my_file6=open(f"{x}","a+")
#         my_file6.write(f"{d}")
#         my_file6.read()
#         my_file6.close()
#     except FileNotFoundError:
#         print("Такого файла не существует")
# elif u==6:
#     try:
#         q=input("Какой файл хотите удалить:")
#         os.remove(q)
#     except FileNotFoundError:
#         print("Такого файла не существует")
# elif u==7:
#     h=input("Название папки:")
#     os.mkdir(h)             # создать папку     
# elif u==8:
#     try:
#         e=input("Какую папку хотите удалить:")
#         os.rmdir(e)
#     except FileNotFoundError:
#         print("Такой папки не существует")
# else:
#     print("В:ведите толко цифры до 8!!!")
# os.rem    ove("("Такого файла не существует")s")            # remove file
# os.rmdir("nnnnnnnnnn")    # remove directory


# words = input("Слова: ")
# for i in words:
# words = input("Слова: ")

# l = words.split()
# q=""
# for i in sorted(l,key=lambda a: len(a)):
#     q = q + " " + i
# print(q)


# words= input("Пишите слова: ").split()
# # print(sorted(map(len,words)))
# max_len = len(words[0])
# for i in range(len(words)):
#     if max_len <= len(words[i]):
#         max_len = len(words[i]) 
#     print((sorted(map(words))))

#Выведется в строке отсортированные в порядке возрастания количества символов слова из введённого пользователем текста
# words = input("Слова").split()
# g=[]
# lens = sorted(map(len, words))
# for i in lens:
#     for y in words:
#         if i == len(y):
#             g.append(y)
#             break
# print(*g)

# my_fun

# s="""QT - один из лучших фреймворков для формирования пользовательского интерфейса.
# Его использует десктопный клиент телеграма, к примеру.А также множество других крупных компаний.
# Этот фреймворк уже давно прошел проверку временем и, конечно же, как вы видели из названия поговорим про версию для Python.
# PyQT это высококлассная библиотека создания пользовательского интерфейса.
# В ней доступны компоненты QT4 и QT5.
# Стоит попробовать и поработать с ней,
# к этому располагает качественная документация и множество реальных примеров."""
# r=lambda j:len(j)
# print(r(s))