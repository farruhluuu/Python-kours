
# from hw15 import mult_numbers


"""Встройные библиотеки"""
"""random()"""

import random
# num1 = random.randint(0,50)
# print(num1)

# import random
# for i in range(6):
#     print(random.randint(0,100))

# f = random.random()
# print(f)
# # a=10
# # for i in
# 6


# s = random.randint(0,10)  
# a =int(input("Угадай число:"))
# while True:
#     # a =int(input("Угадай число:"))
#     if a<s:
#         print("Ваше число меньше моего")
#     elif s<a: 
#         print("Ваше число больше")
#     elif a==s: 
#         print("Да,верно!!")
#         break
#     else: 
#        print("Ведите только числа")
#     a =int(input("Угадай число:"))


# """choice"""

# cours = "itcbootcamp"
# print(cours[random.randint(0,len(cours))])


w="The official home of the Python Programming Language.".replace(" ","").lower()
# print(random.choice(w))
# q =random.choice(w)
# count = 0
# for i in w:
#      if i ==q:
#           count+=1
# print(q)
# print(count)

# """datetime"""

# import datetime

# today = datetime.datetime(2021,12,2,16,42,25)
# print(today)




a=int(input("Введите число: "))
b=''
for i in range(a+1):
    b = b + (str(i) + ' ')*i
print(b[0:a*2])
print(b)



