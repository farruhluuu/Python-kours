# lst=[5,8,2,7,8,8,2,4]
# num=8
# for i in range(len(lst)):
#     if num==lst[i]:
#         print(i)
#         break
# else:
#     print("Отсуствует")



"""1. Создайте класс Factory и внутри создайте 2 метода:
a. Метод engine который возвращает строку "Двигатель создан"
b. Метод bridge который возвращает строку "Ходовая часть создана"
2. Создайте класс Toyota который будет НАСЛЕДОВАТЬ класс Factory. В классе
Toyota создайте методы wheels и windows.
a. Метод wheels возвращает строку "Колёса готовы"
b. Метод windows возвращает строку "Стёкла готовы"
Из класса Toyota вызовите все методы, методы вернут вам сроки(объекты)
Результат каждого метода вставьте в лист"""

# class Faktory:
#     def engine(self):
#         print("Двигатель создан")
#     def bridge(self):    
#         print("Ходовая часть создан")
# class Tayota(Faktory):
#     def wheels(self):
#         print("Калеса готовы")
#     def windows(self):
#         print("Стекла готовы")    
# n=Tayota()
# n.engine()
# n.bridge()        
# n.wheels()
# n.windows()





# """1. Создайте Класс Zoo.
# 2. Инициализируйте класс в объект.
# 3. К объекту Zoo добавьте атрибут animal_1 и присвойте ему значение "Тигр"
# 4. К объекту Zoo добавьте атрибут animal_2 и присвойте ему значение "Бегемот"
# 5. К объекту Zoo добавьте атрибут animal_3 и присвойте ему значение "Жираф"
# 6. В объекте Zoo измените значение атрибута animal_1 и присвойте ему значение
# "Лев".
# 7. К объекту Zoo добавьте атрибут animal_4 и присвойте ему list состоящий из
# animal_2 и animal_3
# 8. В объекте Zoo измените значение атрибута animal_3 и присвойте ему значение
# # "Змея"."""

# class Zoo:
#     def __init__(self,animal_1,animal_2,animal_3):
#         self.aimal_1=animal_1
#         self.aimal_2=animal_2
#         self.aimal_3=animal_3
#         self.aimal_3="Змея"
# zoo=Zoo("Тигр","Бегемот","Жираф",)
# zoo.aimal_1="Лев"
# print(zoo.aimal_1)
# print(zoo.aimal_2)
# print(zoo.aimal_3)


# class Addres:
#     def __init__(self,city,district,home_number):
#         self.city=city
#         self.district=district
#         self.home_number=home_number
# class Proffesion:
#     def __init__(self,proffesion,job_addres,salary):
#         self.proffesion=proffesion
#         self.job_addres=job_addres
#         self.salary=salary
# class Worker:
#     def __init__(self,name,city,district,home_number,proffesion,job_addres,salary):
#         self.name=name
#         self.address=Addres(city=city,district=district,home_number=home_number)
#         self.proffesion=Proffesion(proffesion=proffesion,job_addres=job_addres,salary=salary)

#     def printData(self):
#         print(f"{self.name} livees in {self.address.city}")
#         print(f"{self.name} in district {self.address.district}")
#         print(f"{self.name} live in {self.address.home_number}")
#         print(f"{self.name} is a {self.proffesion.proffesion}")
#         print(f"{self.name} work in the {self.proffesion.job_addres}")
#         print(f"{self.name} gets {self.proffesion.salary}")

# i = Worker("Uluk","Osh","Cheremushki","Baytemirova","python devolper","USA","5000")
# i.printData()

# Создать 2 класса Human и Worker. У класса Human, который 
# принимает в конструкторе name, age, gender. И есть методы геттер и сеттер. 
#  У метода сеттер есть 3 аргумента: name, age, gender. У метода геттер должен вывести сообщение
#   "<Name> is <age> years old. He is <gender>"
# У класса Worker есть конструктор который 
# принимает все атрибуты у класса Human. И есть атрибуты profession,
#  about, который является объектом класса Human. И есть метод show_info, он должен 
# возвращать "My name is <name>. I am <age> years old. I am <gender>. I am a <profession>"
# class Human:
#     def __init__(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
#     def my_get(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
#     def my_set(self):
#         print(f"{self.name} is {self.age} years old. He is {self.gender}")
# class Worker:
#     def my_worker(self,name,age,gender):
#         self.proffesion_about=Human(name=name,age=age,gender=gender)
#     def workersha(self):
#         print(f"My name is {self.proffesion_about.name}. I am {self.proffesion_about.age} years old. I am {self.proffesion_about.gender}.")
# she= Worker ("Ayana","22","Female")
# she.my_worker()


# Создать 2 класса Human и Worker. У класса Human, который принимает в конструкторе name, age, gender. И есть методы геттер и сеттер.  У метода сеттер есть 3 аргумента: name, age, gender. У метода геттер должен вывести сообщение  "<Name> is <age> years old. He is <gender>"
# У класса Worker есть конструктор который принимает все атрибуты у класса Human. И есть атрибуты profession, about, который является объектом класса Human. И есть метод show_info, он должен возвращать "My name is <name>. I am <age> years old. I am <gender>. I am a <profession>"





# my_varible = "ITCbootcamp"

lang_list=["C++","C#","JAVA","PYTHON","JAVASCRIPT"]