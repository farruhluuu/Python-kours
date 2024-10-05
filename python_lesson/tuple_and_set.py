""""Tuple-кортеж"""

# tpl = tuple()         #создать пустой кортеж
# tpl2 = ()                #2- способ

# print(type(tpl))
# print(type(tpl2))

# tpl3 =("True", 454, "python", "book")
# tpl4 =tuple(54, "plus", 587, False)
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

# a  = (1,2,3,4,5)
# a2 = (6,7,8,9)
# lst.append(a)
# lst.append(a2)
# lst.append(a3)
# print(lst[1])


# import sys
# a3 = (10, 11, 12, 13, 14, 15)
# lst = [10, 11, 12, 13, 14, 15]
# mySet = {10, 11, 12, 13, 14, 15}

# size = sys.getsizeof(a3)
# size1 = sys.getsizeof(lst)
# size2 = sys.getsizeof(mySet)

# print(size)
# print(size1)
# print(size2)


"""  SET-множество   """

# Множество (класс set) - это контейнер, который содержит уникальные не
# повторяющиеся элементы в случайном порядке (неупорядоченная коллекция).

# correct_empty_set = {}
# print(type(correct_empty_set))

# mySet = {'c', 'a', 't'}
# # выводится в любом случайном порядке
# print(mySet)


# color_list = ["red", "green", "green", "blue", "purple", "purple"]
# color_set = set(color_list)
# print(color_set) 


# colors = {"red", "green", "blue"}
# # Метод add добавляет новый элемент в множество
# colors.add("purple")


# Добавление элемента, который уже есть в множестве, не изменяет
# это множество
# colors.add("red")
# print(colors)

# st = {'red', 'blue', 'green', 'white'}
# print(st)

# len(s) - число элементов в множестве (размер множества).
# st = {'red', 'blue', 'green', 'white'}
# print(len(st))

# x in s - принадлежит ли x множеству s.

# set.isdisjoint(other) - истина, если set и other не имеют общих элементов.
# st = {'red', 'blue', 'green', 'white'}
# other = {'orange', 'brown', 'purple', 'black', 4}
# new = st.isdisjoint(other)
# print(new)


# set.issubset(other) или set <= other - все элементы первого переменного принадлежат ко второму переменному. Простыми словами все элементы похожи то выведет True иначе False
# st = {'red', 'blue', 'green', 'white'}
# other = {'blue', 'red', 'green', 'white'}
# new = st.issubset(other)
# print(new)

# set.issuperset(other) или st >= other - все элементы второго переменного принадлежат к первому переменному. Простыми словами все элементы похожи 2х переменных то выведет True иначе False

# st = {'red', 'blue', 'green', 'white'}
# other = {'orange', 'brown', 'purple', 'black'}
# new = st.issuperset(other)
# print(new)

# set.union(other, ...) или set | other | ... - объединение нескольких множеств.
# st = {'red', 'blue', 'green', 'white'}
# other = {'orange', 'brown', 'purple', 'black'}
# new = st.union(other)
# print(new)

# set.intersection(other, ...) или set & other & ... - пересечение.
# st = {'red', 'blue', 'green', 'purple', 1,2,3}
# other = {'blue', 'orange', 'brown', 'purple', 'black', 1,2,3}
# new = st.intersection(other)
# print(new)


# set.difference(other, ...) или set - other - ... - множество из всех элементов set, не принадлежащие ни одному из other.

# st = {'red', 'blue', 'green', 'purple'}
# other = {'orange', 'brown', 'purple', 'black'}
# new = other.difference(st)
# print(new)


# set.symmetric_difference(other); set ^ other - множество из элементов, встречающихся в одном множестве, но не встречающиеся в обоих.
# st = {'red', 'blue', 'green', 'purple'}
# other = {'orange', 'brown', 'purple', 'black'}
# new = other.symmetric_difference(st)
# print(new)


# set.intersection_update(other, ...); set &= other & ... - пересечение.
# set.update(other, ...); set |= other | ... - объединение.
# st = {'red', 'blue', 'green', 'purple'}
# other = {'orange', 'brown', 'purple', 'black'}
# other.update(st)
# print(other)

# set.difference_update(other, ...); set -= other | ... - вычитание.
# st = {'red', 'blue', 'green', 'purple'}
# other = {'orange', 'brown', 'purple', 'black'}
# other.difference_update(st)
# print(other)

# set.symmetric_difference_update(other); set ^= other - множество из элементов, встречающихся в одном множестве, но не встречающиеся в обоих.

# set.add(elem) - добавляет элемент в множество.
# st = {'red', 'blue', 'green', 'purple'}
# st.add('white')
# print(st)

# set.remove(elem) - удаляет элемент из множества. KeyError, если такого элемента не существует.
# st = {'red', 'blue', 'green', 'purple'}
# st.remove('red')
# print(st)

# set.discard(elem) - удаляет элемент, если он находится в множестве.
# st = {'red', 'blue', 'green', 'purple'}
# st.remove('red')
# print(st)

# # set.pop() - удаляет первый элемент из множества. Так как множества не упорядочены, нельзя точно сказать, какой элемент будет первым.
# st = {'red', 'blue', 'green', 'purple'}
# st.pop()
# print(st)


# set.clear() - очистка множества.
# st = {'red', 'blue', 'green', 'purple'}
# st.clear()
# print(st)





# students = {'Чынгыз', 'Кудрет', 'Азиз'}



# lst = ['i']
# if 'i' in lst:
#     print('est')