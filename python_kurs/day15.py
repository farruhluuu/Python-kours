# """Тернарный оператор,List comprehension"""
# lst = [5, 8 ,7, 12, 56, 87, 55, 10, 4, 3,]
# lst2 = []
# for i in lst:
#     if i>5:                                       Цикл по элементу
#         lst2.append(i)
#         print(lst2)





# lst = [5, 8 ,7, 12, 56, 87, 55, 10, 4, 3,]
# lst2 = []
# for i in range(len(lst)):                       Цикл по индексу
#     if lst[i]>5:
#         lst2.append(lst[i])
# print(lst2)


# lst = [5, 8 ,7, 12, 56, 87, 55, 10, 4, 3,]
# lst2 = [i for i in lst]
# lst3 = [i for i in lst if i > 5]
# print(lst2)
# print(lst3)




# ls = [[45, 58],[4, 87],[1,2]]
# ls2 = [y for i in ls for y in i]
# # print(ls2)
# ls3 = []
# for i in ls:
#     for y in i:
#         ls3.append(y)
# print(ls3)



# even_ls = [y for i in ls for y in i if y %2==0 and y>3]
# print(even_ls)
# for i in ls:
#     for y in i:
#         if y %2==0:
#             even_ls.append(y)
# print(even_ls)





# t = ["kg", "ru", "en", "kz"]
# t2= [i.upper() for i in t]
# print(t2)



# """Тернарный оператор"""


# num = 3
# if num>3:
#     print("it's good")
# else:
#     print("So good")


# print("it's good" if num>6 else "So good")






# n=5
# print("Yes" if n>6 else "no" )




# b=5
# print("5" if b==5 else "FIZZBUZZ")



"""break, cantinue"""
# r =input("Напишите ваш  язык программирование:")
# while True:
#     if r == "python" and "Python":
    
#         print(r)    
# s = random.randint(0,100)  
# 8
a = "Python"
while True:
    b = input("Введите ваш язык программирования: ").title()
    if a != b:
        input("Введите ваш язык программирования: ").lower()
    else:
        break
# message = "p"
# print(message+"x"+message*2)

# p = "python"
# for i in p:
#     if i == message:
#         continue
#     else:
#         print(i)

# def func1(res):
#     if res ==1:
#         return 1
#     else:
#         return res*func1(res-1)
# print(func1(10))


