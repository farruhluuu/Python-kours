"""циклы,for,while"""

# for i in range(1, 10):
#     if i ==5:
#         print(i)
#     else:
#         print("Неизвестный номер")


# lst = [1, 3, 5, 7, 8, 9]
# count = 0 
# for x in lst:
#     # count = count + x
#     # count
#     count += x
# print(count)








# lst2 = [12, 8, 54, 45, 987, 5]
# count = 0 
# for x in lst2:
#     if x % 2 == 0:
#         count += x
# print(count)  
# print(sum(lst2)) 

# number = int(input("Введите число:"))
# for i in range(1, 10): 
#     print(f"{number} + {i} =", i + number)


# lst3 = range(1, 31)
# s = 1
# s = 1 
# for i in range(1,31): 
#     if i % 5 == 0 and i % 3 == 0:
#         s=s * i
# print(s)
    #    i *= i 
# print(i)





d = 0 
col = 0
for i in range(6,64): 
    if i % 2 == 0 or i % 3 == 0:
        d=d + i
        col = col +1
        print("количевство чисел которые делятя 2,3", i)
print(d)
print("количевство чисел которые делятя 2,3", col)
    #    i *= i 

"""while"""
i = 0
my_lst =[1, 2, 3, 4]
while i < len(my_lst):
    print(my_lst[i])
    i =i + 1
my_lst = [1, 2, 3, 4]
i = 0
sum1 = 0
col = 0
while i < len(my_lst):
    sum1 = sum1 + my_lst[i]
    col =col + 1
    i = i + 1
print("Сумма:",sum1)
print("Количевство:",col )









# my_lst = [1, 2, 3, 4]
# i = 0
# sum1 = 1
# col = 0
# e = 1
# while i < len(my_lst):
#     sum1 = sum1 * my_lst[i]
#     col =col + 1
#     i = i + 1
#     e = e + 1
# print("Произведение:",sum1)
# print("Количевство:",col )
# print("ff",e )



# l = [ 5, 78, -6, 8, -45]
# i = 0
# while i < len(l):
#     if l[i] > 0:
#         print(l[i])
#     i += 1

# i = 1
# while i < 100:
#     print(i)
#     i=i + 2


# Дан одномерный массив целых чисел. Разложить по разным массивам положительные и отрицательные элементы.









# deli = [2,4,5, -45, -67, -4, -8,67, -4,45]
# for i in deli:
#         if i < 0:
#             print(i)

# i = 10
# while i < 101:
#     print(i)
#     i += 1

# gg = input("Введите пороль:")
# pasword ="Исмаилова Бегимай"
# while gg!=pasword:
#     print("Введите правильно")
#     gg=input("Введите пороль:")






# lst = range (0, 100)
# i = 1
# sum = 1
# while i > len(lst):
#      sum = sum + 1 (lst[i])
# print(i)
# sum += 1




# while home_w2>len(home_w3):
#     if home_w2 == home_w3:
#         print(home_w2)
#         home_w2 += home_w3






















