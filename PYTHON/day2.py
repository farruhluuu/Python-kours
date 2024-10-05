import random
import requests

# letter_meals = 'www.themealdb.com/api/json/v1/1/list.php?i=list'
# res = requests.get(letter_meals).json()
# meals = res['meals'][0]['strIngredient']
# print(res)

# url = f"https://covid-api.mmediagroup.fr/v1/cases"
# res  = requests.get(url).json()
# json_covid = res
# for i in json_covid:
#         cofirmedd = i['All']
#         # country = str(i['All']['country'])
#         print(cofirmedd)


# il = []
# url = f"https://covid-api.mmediagroup.fr/v1/cases?"
# res  = requests.get(url).json()
# json_covid = res
# for i in json_covid:
#         il.append(i)
#         print(il[0])




# from ast import Delete
# import  requests

# token_API = f"https://covid-api.mmediagroup.fr/v1/cases"
# covid= requests.get(token_API)
# covid_json=covid.json()
# cheknumber=[]
# chekcountry=[]
# finish={}
# for i in covid_json:
#     cheknumber.append(covid_json[i]['All']['confirmed'])
#     chekcountry.append(i)
# #     print(covid_json[i]['All']['confirmed']i)
# a=max(cheknumber[:-1])
# index = cheknumber.index(a)
# # print(index)
# # print(chekcountry[index])
# for i in range(10):
#     a=max(cheknumber[:-1])
#     index = cheknumber.index(a)
#     finish[chekcountry[index]]=cheknumber[index]
#     chekcountry.pop(index)
#     cheknumber.pop(index)
# print(finish)
# # print(len(finish))


# from collections import Counter
# rr = [23, 32, 23, 32, 44]
# print(Counter(rr))
# text = open("file.txt").read()
# unique = set(text.split())

# for word in unique:
#     print(f'{word}: {text.count(word)}')

# text = [4, 5,645,45,23,3,4 ,4,4, 5, 7]
# unique = set(text.split())

# for word in unique:
#     print(f'{word}: {text.count(word)}')


# array.count("Bob")
# array.count("John")
# dict((x, array.count(x)) for x in set(array) if array.count(x) > 1)
# {'Bob': 2}


# array = ["Bob", "Alex", "Bob", "John"]
# for i in array:
#     arrayy = array.count(i)
# print(i)


# num = 2932
# new1 = num[0][1]
# new2 = num[2][3]
# if new1 < new2:
# print(num[0][1])
# jewels = "aA"
# stones = "aAAbbbb"
# y = jewels, stones
# count = 0
# for i in y:
#     for h in i:
#         if h =="A":
#             count+=1    
# print(count)
# class Solution:
#     def numJewelsInStones(self, jewels: str, stones: str) -> int:
#         stones_count={}
#         count=0
#         for i in stones:
#             if stones_count.get(i,-1)==-1:
#                 stones_count[i]=1
#             else:
#                 stones_count[i]+=1
#         for i in jewels:
#             count+=stones_count.get(i,0)
#         return count
# address = "1.1.1.1"
# a = str.replace(address, ".", "[.]")
# print(a)

# def letter(pk):
#     if pk == '1':    
#         letter_meals = f'www.themealdb.com/api/json/v1/1/search.php?f=v'
#         res = requests.get(letter_meals)
#         jeyson = res.json()
#         meals = jeyson['meals'][0]['strMeal']
#         print(12)
# letter(1)

# rdm = random.choices('abcdefghijklmnopqrstuvwxyz', k=4)
# print(rdm)
# rdm = random.choices('abcdefghijklmnopqrstuvwxyz', k=4)
# lin = len(rdm)
# for oo in rdm:
#     print(oo)




# txt = 'Hello, I am backend developer'
# rep = txt.replace(' ', '')
# print(rep)                        #Hello,Iambackenddeveloper


# txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
# txt2 = "My name is {0}, I'm {1}".format("John",36)
# txt3 = "My name is {}, I'm {}".format("John",36)
# print(txt1)









# inp1 =  input("Введите ваше имя:")
# inp2 = input("Фамилия:")
# txt1 = "My name is {in1}, My lastname {in2}".format(in1 = "John", in2 = 36)
# txt2 = "My name is {0}, My lastname {1}".format(inp1,inp2)
# txt3 = "My name is {}, My lastname {}".format(inp1,inp2)

# print(txt1)



# txt = 'Hello, I am backend developer'
# # rep = txt.replace('8', '  ')
# # print(rep)                        #Hello,Iambackenddeveloper
# length = len(txt)
# print(length)



# lyric = """Look/ 
# ]If ]yo/u had
# One sh]/ot]
# O]r /one op/portu]nity/
# To seize ever/ything yo/u ever /wanted
# In o/ne m]omen/t
# Wou/l]d /yo]u captu/]re it
# Or just] let it/ s]lip?"""

# 1:Вам нужно убрать знак '/' и ']'
# 2:Вывести длину кода

# a = 

# print(lyric.replace('/', '').replace(']',''))
# print(len(lyric.replace('/', '').replace(']','')))

# вернуть код    ctrl + z  обратно удалить ctrl + y или ctrl + shift + z


# age = int(input("Введите ваш возраст:"))
# if age > 50 and age == 51:
#     print("Вы не можете войти")
# else: 
#     print("Добро пожаловать")





# Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).


# tt = 'dfga', 'aergaeg', 234
# print(type(tt))













from datetime import datetime
import time

def list_check():
    start_time = datetime.now()
    lst = [23, 23, 23,2,12,3, 132,123,12,3,123,132,123,12,3,123,123,12,3,123,12,3,123,12,34,1234,132,5,1235,134,51,5,1,51,51,5]
    print(lst)
    print(datetime.now() - start_time)

def tuple_check():
    start_time = datetime.now()
    tuple = (23, 23, 23,2,12,3, 132,123,12,3,123,132,123,12,3,123,123,12,3,123,12,3,123,12,34,1234,132,5,1235,134,51,5,1,51,51,5)
    print(tuple)
    print(datetime.now() - start_time)


# def set_check():
#     start_time = datetime.now()
#     st = {23, 23, 23,2,12,3, 132,123,12,3,123,132,123,12,3,123,123,12,3,123,12,3,123,12,34,1234,132,5,1235,134,51,5,1,51,51,5}
#     print(st)
#     print(datetime.now() - start_time)

# tuple_check()
# list_check()
# set_check()






"""dictionary-словарь-хеш таблица"""



# # dict = 9
# # print(type(dict))
# dct = dict({
#     "ru":"Russian",
#     "kg":"Kyrgyzstan",
#     9:(5,6,3,23)
#     })
# dct['ru'] = 'USA'
# # print(dct)
# dct2 = {"en":"English",
#  "dictionary":{
#     'dictionary2':{
#         'dictionary3':''
#     }
#  },
#   5:"five",
#    True:[545,87,False],
#    "tuple": (54,8532)}
# print(dct2)


# menu = {}

# menu['Шашлык'] = 90
# menu['Манты'] = 50
# del menu['Манты']
# menu['Лагман'] = 190
# menu['Пельмени'] = 150
# menu['Напитки'] = {'Fanta':200, 'Coca-Cola':90, 'Дюшес':20}

# #  Лагман, Шашлык, Дюшес
# print(menu)


my_dictionary = {}
my_dictionary['run'] = 'бегать'
my_dictionary['sleep'] = 'спать'
my_dictionary['drink'] = 'пить'
my_dictionary['jump'] = 'прыгать'
my_dictionary['swim'] = 'плавать'

# Напишите программу которая принимает 1 слово на анг и выводит перевод на русском 


accounts = {}
accounts['cat@gmail.com'] = 'ko3a56ear3457sh73ka'
accounts['run@gmail.com'] = 'b/e/246g26at'
accounts['swim@gmail.com'] = 'p/lajhkjv/at'
accounts['jump@gmail.com'] = 'pr234y234gat'
accounts['sleep@gmail.com'] = 's23pa56234623t'
tpl = accounts.items()
# print(type(tpl))
for i in tpl:
    print(i)


















# dct2['tuple'] = 345
# print(dct2)

# dct2[5] = "пять"     # изменить значение
# print(dct2)

# dct2[True][2] = 15
# print(dct2)

#print(dct2[True][1]+dct2[True][2]+dct2[True][0])
# dct2[True][1] = (dct2[True][1]+dct2[True][2]+dct2[True][0])
# print(dct2)

# del dct2["tuple"]    #удаление
# print(dct2)





# dict.clear() - очищает словарь.

# dict.copy() - возвращает копию словаря.

# dict.get(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а возвращает default (по умолчанию None).

# dict.keys() - возвращает ключи в словаре.

# dict.pop(key[, default]) - удаляет ключ и возвращает значение. Если ключа нет, возвращает default (по умолчанию бросает исключение).

# dict.popitem() - удаляет и возвращает пару (ключ, значение). Если словарь пуст, бросает исключение KeyError. Помните, что словари неупорядочены.


# dict.values() - возвращает значения в словаре.

students = {'Bektur', 'Chyngyz', 'Faiz', 'Kudret', 'Aziz', 'Gulzhigit', 'Madina'}



#Problem4:

    # Пример:
    # Ввод: 
    # admin
    # Вывод:
    # Добро пожаловать, программист!
    # Программа завершила своё исполнение...










accounts = {}
accounts['cat@gmail.com'] = 'ko3a56ear3457sh73ka'
accounts['run@gmail.com'] = 'b/e/246g26at'
accounts['swim@gmail.com'] = 'p/lajhkjv/at'
accounts['jump@gmail.com'] = 'pr234y234gat'
accounts['sleep@gmail.com'] = 's23pa56234623t'





