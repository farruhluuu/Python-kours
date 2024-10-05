# 1)
# С помощью циклов while напишите код, который никогда не завершится. Например, этот фрагмент кода бесконечно печатает, ((когда он закончится?))



# home_w = ("когда он закончится?")

# while home_w:
#     print(home_w)











# 2)
# Напишите программу для печати таблицы умножения заданного числа

# number = int(input("Введите число:"))

# for i in range(1,11):
#     # print(f'{number}*{i} = {number * i}')
#     # print(i, "*", number, "=",i*number)
#     print("{0} * {1} = {2}".format(i,number,i*number))




# list = [10, 20, 30, 40, 50]
# list1=[]
# for i in range(1,len(list)+1):
#     list1.append(list[-i])
# print(list1)

# i=1
# while i<len(list)+1:
#     list1.append(list[-i])
#     i+=1
# print(list1)












# """Двухмерные массивы """
# from typing import Counter


# my_list = [45, 87, 789, 44]
# my_list2= [[45,78,45,12],
#             [5, 787, 78, 15],
#             [8, 2, 45, 877]]
# # print("количевсто всех элементов:",len(my_list2))
# Count=0
# for i in range(len(my_list2)):
#         # print(len(my_list2[i]))
#     Count+= len(my_list2[i])
# print(Count)

# my_list2= [[45,78,45,12],
#             [5, 787, 78, 15],
#             [8, 2, 45, 877]]
# summ=0
# for i in range(len(my_list2)):
#     for y in range(len(my_list2)):
#         print(my_list2[i][y])
#         summ += my_list2[i][y]
# print(summ)



# my_list3=   [[45,-78,-45,12],
#             [5, -787, 78, 15],
#             [8, 2, 45, 877]]
# v=0
# summ =0
# for i in range(len(my_list3)):
#     for y in range(len(my_list3)):
#         if my_list3[i][y]<0:
#             v=v+1
#             summ = summ + my_list3[i][y] 
#             print(my_list3[i][y])
# print(v)
# print(summ)

"""Функции-function"""

# print("Текст")
# def my_function():
#     print("my_function")
# my_function()
# my_function()





# def my_sum():
#     a = 5 
#     b = 7
#     print(a+b)
# my_sum()



# def my_sub():
#     a = 5 
#     b = 7
#     print(a-b)
# my_sub()



# def my_mult():
#     a = 5 
#     b = 7
#     print(a*b)
# my_mult()



# def my_div():
#     a = 5 
#     b = 7
#     print(a/b)
# my_div()




# def my_sum2():
#     a =4
#     b= 2
#     c = a+ b
#     return c 
# print(my_sum2())


# def sum_of_digit(a, b, c):
#     print(a+b+c)
# sum_of_digit(5,6,9)


# def func(num):
#     ls = []
#     for i in range(num):
#         ls.append(i)
#     print(ls[::-1])
# func(9)







def my_title(a):
    print(len(a.split()))
a = "Python"
my_title(a)





