# lts2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

"""args*-Позиционные элементы**kwargs-Именнованные элементы"""
# lst = [45, 85, 62, 17]
# print(*lst, sep="-")

# print(lst)

# def  my_func(a,lst):
#     z=0
#     for i in lst:
#         z+=i
#         print(z+a)
# my_func(5,[1,2,3,4])


# def  my_func(a,lst):
#     z=a
#     for i in lst:
#         z+=i
#         print(z)
# my_func(5,[1,2,3,4])


# def my_func2(a, *lst):
#     sum=a
#     for i in lst:
#         sum+=i
#     print(sum)
# my_func2(5,1,2,3,4,)


# """**kwargs"""
# def my_fanc3(*g,**h):
#     print(*g)
#     for i in h.values():
#         print(i)

# my_fanc3(4,5,6,7, name="Anna",age=16)

# def my_u(a,*args):
#     sum=0
#     for i in args:
#         if i % 2==0:
#             sum+=i
#     print(sum-a)
# my_u(7,4,3,2,1)



# def my_fanc3(**h):
#     print(h)
#     for i in h:
#         print(i,"-",h[i])

# my_fanc3(name="Джон",Surname="Вуд",age=16,Phone_number=123456789)




# def my_func2(*lst):
#     sum=0
#     for i in lst:
#         sum+=i
#     print(sum)
# my_func2(3,2)
# my_func2(4,5,6,7)
# my_func2(1,2,3,5,6)


# def my_func1(n):
#     for i in range(1,n):
#         print(i)
# my_func1(9)


# """Traceback"""
# a=5
# b=0
# if b==0:
#     print("на ноль делить нельзя")

# print(a+b)
# print(a*b)
# print(b/a)


# if b==0:
#     raise ZeroDivisionError("на ноль делить нельзя")
#     # print("на ноль делить нельзя")
# else:
#     print(a/b)


def summ(a,b):
    if isinstance (a, str):
        raise TypeError ("Тип данных должен быть 'int'")
    if isinstance (a, bool):
        raise TypeError ("Тип данных должен быть 'int'")
    if isinstance (b, bool):
        raise TypeError ("Тип данных должен быть 'int'")
    if isinstance (b, str):
        raise TypeError ("Тип данных должен быть 'int'")
    print(a+b)
summ("5",5)




