"""ООП - Обьектно -ориетированное программираование"""
"""В ООП есть 4 консептции"""
# Наследование 
# Абстрактсия-Композиции
# Полиморфизм
# Инкапуляция
class Animals:
    feet=4
    tail=1
    head=1
    ears=2
    eyes=2
    def __init__(self,name,colour):
        self.name=name
        self.colour=colour
    def run(self):
        self.feet=2
        print(f"he runs very fast, it has {self.feet} feet")
cat = Animals("Мурка","Черный")
print(cat.name)
print(cat.colour)
print(cat.tail)
cat.run()


#   Наследование
class Douth:          #Родительский класс
    muka=600
    salt=2
    butter=200
    water=300

    def mix(self):
        print("Mix all recepts")

class Samsy(Douth):         #Дочерный класс
    eggs=2

samsy = Samsy()
samsy.mix()
print(samsy.muka)



class Pie(Douth):
    sugar = 250
    milk = 200
    vanilin =5
    bakingPower=5
pie = Pie()
pie.mix






class Venchile:
    pass


class Car(Venchile):
    pass


class Plane(Venchile):
    pass


class RaceCar(Venchile):
    pass


class Boat(Venchile):
    pass





class Person:

    def __init__(self,name,surname,gender="male"):
        self.name=name
        self.surname=surname
        if gender == "male" or gender =="female":
            self.gender=gender
        else:    
            print("Не знаю, что вы имели ввиду?")
            self.gender="male"
    def __str__(self):
        if self.gender=="male":
            return f"Гражданин {self.surname} {self.name}"
        elif self.gender=="female":
             return f"Гражданка {self.surname} {self.name}"
per = Person("Владимир","Навальный","male")
print(per.gender)
print(per)






class Publication:
    def __init__(self,name,date,pages,library,type):
        self.name=name
        self.date=date
        self.pages=pages
        self.library=library
        self.type=type
    
class Book(Publication):
    def __init__(self,type="book"):
        self.type=type

class Magazine(Publication):
    def __init__(self,type="magazine"):
        self.type=type

    
class Newspapper(Publication):
    def __init__(self,type="newspaper"):
        self.type=type
    











# class Latter:
#     vowel = ["a","e","i","o","u","y"]
#     def __init__(self):
#         self.surname=surname
#         if gender == "male" or gender =="female":
#             self.gender=gender
#         else:    
#             print("Не знаю, что вы имели ввиду?")
#             self.gender="male"
#     def __str__(self):
#         if self.gender=="male":
#             return f"Гражданин {self.surname} {self.name}"
#         elif self.gender=="female":
#              return f"Гражданка {self.surname} {self.name}"
# per = Person("Владимир","Навальный","male")
# print(per.gender)
# print(per)












