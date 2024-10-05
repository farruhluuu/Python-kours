

# a = int(input("Ведите 1-число:"))
# znak = input("Введите знак: ")
# b = int(input("Ведите 2-число:"))

# if znak == '+':
#     с = a + b
#     print("Результат: ", a + b)
# elif znak == "-":
#     c = a + b
#     print("Результат: ", a - b)
# elif znak == "*":
#     c = a * b
#     print("Результат: ", a * b)
# elif znak == "/":
#     c = a / b
#     print("Результат: ", a / b)
# else:
#     print("Выбрана неверная операция")

# A=0 
# B=2
# C=5
# A1=A + B
# B1 =A + C
# C1 = A +B + C
# A=A1
# B=B1
# C=C1
# print(A)
# print(B)
# print(C)
# 3

# a = int(input("Ведите см:"))
# b = a+a+a+a
# print("Периметр квадрата",a+a+a+a)

# sequence_0 = (14,10,35,45,60,70,90,0,105,150,10.0,45.0,70,0)
# sequence_1 = (14,10,35,45,60,70,90,0,105,150,70)
# sequence_2 = (14,10,35,45,60,70,90,0,105,150,10.0,45.0,70,0.0)
# sequence_3 = (14,10,35,45,60,70,90,0,105,150,10.0,45.0,70)

# haca1 = set(sequence_0)
# if len(sequence_0) == len(haca1):
#     print("1-Последовательность уникален")
# else:
#     print("1-Не уникален")
# haca2 = set(sequence_1)
# if len(sequence_1) == len(haca2):
#     print("2-Последовательность уникален")
# else:
#     print("2-Не уникален")

# haca3 = set(sequence_2)
# if len(sequence_2) == len(haca3):
#     print("3-Последовательность уникален")
# else:
#     print("3-Не уникален")


# haca4 = set(sequence_3)
# if len(sequence_3) == len(haca4):
#     print("4-Последовательность уникален")
# else:
#     print("4-Не уникален")


# keys_values = ('one', 1,'two', 2, 'three', 3,  'four', 4, 'five', 5,'six', 6,'seven',  7,  'eight', 8, 'nine',9,'ten', 10,'eleven',  11,'twelve',12)
# pairs = {}

# for i in  range (len(keys_values)):
#     if i % 2==0:
#         pairs[keys_values[i]] = keys_values[i+1]
# print(pairs)

# num = int(input("Введите 4х значное число"))
# num = str(num)
# if len(num)==4:
#     if int(num[0])>int(num[1])>int(num[2])>int(num[3]):  
#             print("расположены по убыванию")
# else:
#     print("Введите 4х значное число")


def max_in():
    a = int(input("Введите цифру:"))
    b = int(input("Введите цифру:"))
    c = int(input("Введите цифру:"))
    if a<b<c:
        print("Самое большое число из этих чисел",c) 
    elif b<a<c:
        print("Самое большое число из этих чисел",c) 
    elif a<c<b:
        print("Самое большое число из этих чисел",b) 
    elif c<a<b:
        print("Самое большое число из этих чисел",b) 
    elif b<c<a:
        print("Самое большое число из этих чисел",a) 
    elif c<b<a:
        print("Самое большое число из этих чисел",a) 
    else:
        ("Введите только числа")
max_in()