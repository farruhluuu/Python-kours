
import os
u=int(input("Для создания введите 1:\nДля записи введите 2:\nДля чтение введите 3:\nДля добавление введите 4:\nДля добавления и чтения введите 5:\nДля удаления файла введите 6:\nЕсли хотите создать папку введите 7:\nЕсли хотите удалить папку введите 8:"))
if u == 1:
    file_name=input("Напишите название файла для создания:")
    try:
        new = open(file_name, "x")
        print("Файл создан")
    except FileExistsError:
        print("Такой файл уже создана")
elif u == 2:
    f=input("Что хотите:")
    my_file2= open("new_file", "w")
    my_file2.write(f"{f}\n")
    my_file2.close()
elif u == 3:
    my_file5= open("new_file","r")
    print(my_file5.read())

elif u == 4:
    o=input("Что хотите:")
    my_file3 = open("new_file", "a")
    my_file3.write(f"{o}")
    my_file3.close
elif u == 5:
    d=input("Что хотите:")
    my_file6=open("my_file.txt","a+")
    my_file6.write(f"{d}")
    my_file6.read()
    my_file6.close()
elif u==6:
    try:
        q=input("Какой файл хотите удалить:")
        os.remove(q)
    except FileNotFoundError:
        print("Такого файла не существует")
elif u==7:
    h=input("Название папки:")
    os.mkdir(h)             # создать папку
elif u==8:
    try:
        e=input("Какую папку хотите удалить:")
        os.rmdir(e)
    except FileNotFoundError:
        print("Такой папки не существует")
    else:
        print("В:ведите толко цифры до 8!!!")