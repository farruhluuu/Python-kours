lst = [15, 98, 8, True, "Good", 8, False]
#      0   1    2  3      4          5
#                                0    1      2 
# print(lst[5][2])    #False\
 
# lst2 = ["Take","dog","eggs"]

# lst.append(lst2)

# lst.extend(lst2)
# print(lst)


# lst4 = ["Take","dog","eggs"]

# print(lst3+lst4)
# lst3.insert(1,"cat")    Добовляет слово
# print(lst3)
# lst3 = ["Take","dog","eggs"]
# lst3.remove("Take")
# print(lst3)

# lst3.pop(2)
# print(lst3)


# lst9 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# print(len(lst9))
# lst9
# print(lst9[4:15])
# print(lst9[:8:-1])




# firt_list = [45, 78, 87, True]
# firt_list[0] = "Language"
# print(firt_list)
# first_element = firt_list[0]
# third_element = firt_list[3]
# second_elevent = firt_list[1]
# firt_list[0] =third_element
# firt_list[1] =first_element
# firt_list[3] =second_elevent
# print(firt


# old_list = [5, 6, 8, 99, 4, 62, 73]
# first_element = old_list[0]
# seventh_element = old_list[6]
# old_list[0] = seventh_element
# old_list[6] = first_element
# print(old_list)

# 
# """"Tuple-кортеж"""

# tpl = tuple()         #создать пустой кортеж
# tpl2 = ()                #2- способ

# print(type(tpl))
# print(type(tpl2))

tpl3 =("True", 454, "python", "book")
# tpl4 =tuple(54, "plus", 587, False)
print(tpl3)
# print(tpl3)
# print(tpl4)
# print(tpl3[0])
# print(tpl3[-1])


# tpl7 = (True, 0.5, 3, "python",[54, 3, "css"])
# print(tpl7[0])
# print(tpl7[4])
# print(tpl7[2])

# tpl7 = (True, False, '3')
# print(tpl7[0])
# print(tpl7[1])
# print(tpl7[2])

# a  = (1,2,3,4,5,)
# a2 = (6,7,8,9,)
# a3 = (10,11,12,13,14,15)
# lst = []
# lst.append(a)
# lst.append(a2)
# lst.append(a3)
# print(lst[2][2])

    # Дан список [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
      # Ваша задача:
      # - разделите список на 3, заключите третий список внутрь второго, а второй внутрь первого [1...33,[34...66, [67..100]]]


#Problem1:
    # Напишите программу, которая удаляет последний элемент из массива: lst = [9, 5, 7, 4, 2, 6, 8, 1]




#Problem2:
    # Напишите программу, которая считает количество похожих элементов, в этом случае наш элемент "5" из массива: lst = [9, 5, 7, 5, 2, 6, 5, 1, 9, 54]




# old_list = [5, 6, 8, 99, 4, 62, 73]
# first_element = old_list[0]
# seventh_element = old_list[6]
# old_list[0] = seventh_element
# old_list[6] = first_element
# print(old_list)


# a =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33]
# a2 =[34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67] 
# a3 =[68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
# lst = []
# lst.append(a3)
# lst.append(a2)
# lst.append(a)
# print(lst)



# lst = [9, 5, 7, 4, 2, 6, 8, 1]
# lst.pop()
# print(lst)


# lst = [9, 5, 7, 5, 2, 6, 5, 1, 9, 54]
# print(lst.count(5))


#          0   1   2  3   4  5   6  7  8  9  10
# numbers = [55, 89, 6, 55, 8, 6, 6, 44, 3, 5, 7, 3,]
# print(numbers.count(55))
# print(numbers.count(8))
# print(numbers.count(6))
# print(numbers.count(3))
# print(len(numbers))
# print("Последнее число",numbers[10])
# print(numbers.index(55))
# numbers.remove(6, 5, 4, 3)
# print(numbers)



