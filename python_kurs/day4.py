"""List - Список - Массив"""



a = 56
b = 55.2 
c = "Text"
# list - Список
#       0              1          2            
lst = ['Картофель', "Морковь", 'Томат']
# print(lst.index("Томат"))
# lst.append('Огурец')
# lst.clear()
# print(lst.count('Томат'))
# lst.remove('Томат')
# lst.pop(2)
# print(lst)
# print(len(lst))


# 1 список с именами учащихся
# 2 входные данные с именем
# 3 выводит в консоль список 
# 4 очищает список
# 5 список с этим именем
# 6 На каждом шаге выводить длину списка





#      -4   -3    -2       -1
# print(type(lst))



# print(lst[2])
# print (lst[-2])
# # способ
# lst2 = list([54,65,True, False])
# print(type(lst2))
# print(lst2)




















# lst.append("Web site")
# print(lst)

# name = ("Aida")
# lst.append(name)
# lst.append(545)
# lst.append(True)
# lst.append("True")
# print(len(lst))
# print(lst)

# #2 способ 
#  lst2 = list([53, True, False, 55.4]) 
# emty_lst = [] 
# emty_lst2 = list[]





# animals =[] 
# # # 0    1    2    3    4
# # animals.append("Лев")
# # animals.append("Пинггвин")
# # animals.append("Утка")
# # animals.append("Змея")
# # animals.append("собака")
# # print(len(animals))
# # print(animals[4]) 


# #          0   1   2  3   4  5   6  7  8  9  10
# numbers = [55, 89, 6, 55, 8, 6, 44, 3, 5, 7, 3,]
# print(numbers.count(55))
# print(numbers.count(8))
# print(numbers.count(6))
# print(numbers.count(3))
# print(len(numbers))
# print("Последнее число",numbers[10])
# print(numbers.index(55))
# numbers.remove(6)
# print(numbers)

# numbers.pop(5)
# print(numbers)
# numbers.insert(4, 66)    #  вставляет в индекс число
# print(numbers)


# a = [1,2,3,4]
# b = [6,7,8,9]

# a.append(b)       #1, 2, 3, 4, 5, [6, 7, 8, 9]]
# print(a)

# a.extend(b)       #[1, 2, 3, 4, 5, [6, 7, 8, 9], 6, 7, 8, 9]
# print(a)


# a.clear   #чистка
#[1, 2, 3, 4, 5, [6, 7, 8, 9], 6, 7, 8, 9]

#problem 1
# Определить високосный год или нет
# Если год не делится на 4, значит он обычный.
# Иначе надо проверить не делится ли год на 100.
# Если не делится, значит это не столетие и можно сделать вывод, что год високосный.
# Если делится на 100, значит это столетие и его следует проверить его делимость на 400.
# Если год делится на 400, то он високосный.
# Иначе год обычный.





# a = (input("сколько дней в этом году?:"))
# print (100/a)
# if type(a) ==float:

#     print("Этот год обычный")

# if type(a) == int:

#     print("Этот год вискосный")

# else:
#     print("Команда неправильна")
    



# age = int(input("Сколько дней в этом году?"))
# if age/4:
#     print(age/4)
#     type(age) == float
#     print("Это обычный год")
# elif type(age) == int:
#     print("Этот год високосный")
# else:
#     print("Введи правильную цифру!")


# a = int(input("Введите число"))
# b = int(input("Введите число"))
# c = int(input("Введите число"))


# if a >= b and a > c:
#     if b >= c:
#         print(b)
#     else:
#         print(c)
# elif b >= a and b >= c:
#     if a <= c: 
#         print(a)
#     else:
#         print(c)
# elif b >= c and b >= c:
#     if b > a :
#         print(b)
# else:
#     print(a)







# num = input("Введите пароль: ")

# pr = num.isdigit() or num.isalpha() or len(num) < 8

# if pr:
#     print("Введите другую пароли")
# elif 8<len(num)<=10:
#     print("Ваш пароль логкий")
# elif 10<len(num)<=12:
#     print("Ваш пароль нормалный")
# elif 12<len(num)<=15:
#     print("Ваш пароль сложный")
# else:
#     print("пароль очень длинные")
#     print("Введите другую пароли")






















################# Method  list

# append()  Adds an element at the end of the list
# d = 'qwrew'
# d = '23'


         #0      #1   #2       #3
# lst = ['qwerty', 34, 345.46, True]
#         #-4

# print(lst[::-1])
# lst = list[]


# fruits = ["apple", "banana", "cherry"]


# fruits.append(['apple', 'banana', 'cherry', 'orange'])
# print(fruits)                  # ['apple', 'banana', 'cherry', 'orange']






# clear()  Removes all the elements from the list
# fruits = ["apple", "banana", "cherry"]
# fruits.clear()
# print(fruits)                       # []



# copy()  Returns a copy of the list
# fruits = ["apple", "banana", "cherry"]
# x = fruits.copy()
# print(x)                            # x = ['apple', 'banana', 'cherry']


# count()  Returns the number of elements with the specified value
fruits = ["apple", "banana", "cherry" ,"cherry", "cherry"]
x = fruits.count("a")
print(x)                              # 1



# extend()  Add the elements of a list (or any iterable), to the end of the current list
# fruits = ['apple', 'banana', 'cherry']
# cars = ['Ford', 'BMW', 'Volvo']
# fruits.extend(cars)
# print(fruits)                   # ['apple', 'banana', 'cherry', 'Ford', 'BMW', 'Volvo']




# index()  Returns the index of the first element with the specified value
# fruits = ['apple', 'banana', 'cherry']
# x = fruits.index("apple")
# print(x)                               



# insert()  Adds an element at the specified position
# fruits = ['apple', 'banana', 'cherry']
# fruits.insert(0, "orange")
# print(fruits)                           #['apple', 'orange', 'banana', 'cherry']



# pop()  Removes the element at the specified position
# fruits = ['apple', 'banana', 'cherry']
# fruits.pop()
# print(fruits)                        

# remove()  Removes the first item with the specified value
# fruits = ['apple', 'banana', 'cherry']
# fruits.remove("banana")
# print(fruits)                         # ['apple', 'cherry']


# reverse()  Reverses the order of the list
# fruits = ['apple', 'banana', 'cherry']
# fruits.reverse()
# print(fruits)                          # ['cherry', 'banana', 'apple']


# sort()  Sorts the list

# cars = [5, 4, 1, 8]
# cars.sort()
# print(cars)                                # [1, 4, 5, 8]





# cars = [5, 4, 1, 8]
# sum = sum(cars)
# print(sum)   



# num = int(input("Число: "))
# s=str(num).isdigit()
# if s and num<13:
#     if 3 <= num <= 5:
#         print("Жаз")
#     elif 6 <= num <= 8:
#         print("Жай")
#     elif 9 <= num <= 11:
#         print("Куз")
#     elif not(12 < num >=2):
#         print("кыш")
# else:
#     print("Толко Положительные числа и не больше 12")
