# # Напишите функцию Python, чтобы найти максимальное из трех чисел 
# def max_in():
#     a = int(input("Введите цифру:"))
#     b = int(input("Введите цифру:"))
#     c = int(input("Введите цифру:"))
#     if a<b<c:
#         print("Самое большое число из этих чисел",c) 
#     elif b<a<c:
#         print("Самое большое число из этих чисел",c) 
#     elif a<c<b:
#         print("Самое большое число из этих чисел",b) 
#     elif c<a<b:
#         print("Самое большое число из этих чисел",b) 
#     elif b<c<a:
#         print("Самое большое число из этих чисел",a) 
#     elif c<b<a:
#         print("Самое большое число из этих чисел",a) 
#     else:
#         ("Введите только числа")
# max_in()


# Напишите функцию Python для суммирования всех чисел в списке.
# def my_summ(l):
#     Summ = 0
#     for i in l:
#         Summ = Summ + i
#     return Summ

# print(my_summ([1,3,5,7,9]))
     
# Напишите программу Python для переворота строки

# --------
# Пример строки: 123qweasd
# Ожидаемый результат: dsaewq321
# keys_values = ('one', 1,'two', 2, 'three', 3,  'four', 4, 'five', 5,'six', 6,'seven',  7,  'eight', 8, 'nine',9,'ten', 10,'eleven',  11,'twelve',12)
# pairs = {}
# a = ("123qweasd")
# b = ()
# for i in  range (len(a)):
#     if i % 2==0:
#         b[a[i]] = a[i+1]
# print(b)
# Напишите функцию Python, которая принимает список и возвращает новый список с уникальными элементами первого списка




# Напишите функцию Python для умножения всех чисел в списке


# def my_pro(l):

#      my_lst = [1, 2, 3, 4]
#      i = 0
#      sum1 = 1
#      while i < len(my_lst):
#           sum1 = sum1 * my_lst[i]
#           # i = i + 1
#      print("Произведение:",sum1)
#      my_pro(my_lst)


# from typing import List


# def reverse_text(txt):
#      return txt[::-1]
# print(reverse_text("123qweasd"))




# from typing import List


# l = [5,6,5,7,7]

# def my_set(lst):

#        my_sets =  set(lst)
#        return list(my_sets)
# print(my_set(l))



# course = "itcbootcamp"
# d={}
# count = 0 
# for i in course:
#      if i == "o":
#           count+=1
# d["o"]=count
# # print(count)
# # print(d)
# count = 0 
# for i in course:
#      if i == "i":
#           count+=1
# d["i"]=count
# # print(count)
# # print(d)
# count = 0 
# for i in course:
#      if i == "b":
#           count+=1
# d["b"]=count
# # print(count)
# # print(d)
# count = 0 
# for i in course:
#      if i == "t":
#           count+=1
# d["t"]=count
# # print(count
# # print(d))
# count = 0 
# for i in course:
#      if i == "c":
#           count+=1
# d["c"]=count
# # print(count)
# # print(d)
# count = 0 
# for i in course:
#      if i == "a":
#           count+=1
# d["a"]=count
# # print(count)
# # print(d)
# count = 0 
# for i in course:
#      if i == "m":
#           count+=1
# d["m"]=count
# # print(count)
# # print(d)
# count = 0 
# for i in course:
#      if i == "p":
#           count+=1
# d["p"]=count
# print(count)
# print(d)


def mult_numbers(l):
     mult = 1
     for i in l:
          mult *= i
     return mult
print(mult_numbers([45, 1, 2, 5, 8]))