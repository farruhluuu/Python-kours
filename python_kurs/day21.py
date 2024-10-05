# class Counter:
#     # def __init__(self,count=0):
#     #     self.count=count
#     def start_from(self,count=0):
#         self.count=count
#     def increment(self):
#         self.count=self.count + 1
#         print(self.count)
#     def display(self):
#         print("Текущее значение счетчика=",self.count)
#     def reset(self):
#         self.count=0
# counter=Counter()
# counter.start_from(7)
# counter.display()
# counter.increment()
# counter.display()
# counter.reset()
# counter.display()


# """Принцыпы ООП-Инкапсуляция"""

# #Инскапсуляция - это упаковка данных и фунции, работающих  с этими данными
# # в один компонент и ограничение доступа к некотрорым компонетам обьекта 


# #Инкапсуляция - скрытие информации 

# #есть 3 уровня доступа к данным:

# # * публичный (public, нет особого синтаксиса , Pulik data)
# # * защишеный (protekted, одно нижнее подчеркиванеи  в начале названия, _ProtectedData)
# # * приватный (private, два нижних подчеркивание в начале названия,privatData)



# class Bankomat:
#     def __init__(self,name,_id,__password):
#         self.name = name
#         self._id=_id
#         self.__password=__password
#     def publik_Method(self):
#         print(f"Пользователь:{self.name}")
#     def _protektedMethod(self):
#         print(f"Пользователь:{self.name}, \nid: {self._id}")
#     def __privateMethod(self):
#         print(f"Пользователь:{self.name}, \nid: {self._id} \nпороль:{self.__password}")
# bank = Bankomat("Alex","1234567","qwerty54321")
# bank.publik_Method
# bank._protektedMethod
# # bank.__privateMethod
# # bank.__privateMethod Выдал ошибку
# bank._Bankomat__privateMethod()


# """Гетттеры и Сеттеры"""
# #get-Получить 
# #set-передать,начать,принимать


# class Number:
#     def set(self,number):
#         self.n=number
#     def get(self):
#         return self.n
# num=Number()
# num.set(5)
# print(num.get())








# class Salary:
#     def set(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def get(self):
#         return f"Имя:{self.name} Зарабатывает за месяц:{self.salary}"
#     def CountOfYear(self):
#         return f"Имя:{self.name} Зарабатывает за год:{self.salary*12}"

# salary = Salary()
# salary.set("Alex", 300)
# print(salary.get())
# print(salary.CountOfYear())




# class UserMail:
#     def __init__(self,login,__email):
#         self.l=login
#         self.__e=__email
#     def set_email(self):
#         i=self.__e("@")
#         n=self.e[0:1]
        

#     def get_email(self):









        # """
        # :type address: str
        # :rtype: str
        # """

