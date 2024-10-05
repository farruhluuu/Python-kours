# 1) Создать класс Phone, у него должен быть атрибут batteryLife, изначальное значение которого равно 100% и метод turnOn(), который при вызове понижает процент заряда телефона на 10%, также должен быть метод charge(), при вызове которого заряд повышается на 10%, но главное, нельзя чтобы он заряжал его больше чем на 100%.
class Phone:
    def __init__(self,batterife=100):
        self.batterlife=batterife
    def turnOn(self,p):
        self.batterlife=self.batterlife - p
        if self.batterlife>=0:
            print(self.batterlife,"%")
        else:
            print("Ваш телефон разряжен")
    def charge(self,p):
        self.batterlife=self.batterlife + p
        if self.batterlife>=100:
            print(self.batterlife,"%")
        else:
            print("Ваш телефон заряжен")
iphone = Phone(50)
iphone.turnOn(53)
iphone.charge(30)
# 2) Создать класс Student с атрибутом student = True, он должен быть родительным классом четырех переменных. У переменных Alex, Sony, Ann, Debra должен быть атрибут возраста, класса в школе (или курса университета) и название учебного заведения.
# class Student:
#     student=True
# study=Student


# class Alex(Student):
#     year=16 
#     cours=1
#     faculty="programmer"
# alex=Alex

# class Sony(Student):
#     year=18
#     cours=3
#     faculty="programmer"
# sony=Sony


# class Debra(Student):
#     year=13
#     Class=8
#     school="Kerme-Too"
# sony=Sony


# class Ann(Student):
#     year=11
#     Class=5
#     school="Cholponbay Tuloberdiev"
# sony=Sony

# 3) Создать класс Band, у него должны быть 4 атрибута, members, albums, songs, listenings. в Members должны быть записаны члены этой музыкальной группы, в Albums названия всех альбомов, в Songs 10 песен группы и в Listenings количество прослушиваний. Вам надо записать минимум 3 группы с этим классом.
# class Band:
#     members=4
#     albums=6
#     songs=23
#     listenings=3600000
# band=Band

# class Nirvana:
#     members=6
#     albums=3
#     songs=17
#     listenings=2300000
# nirvana=Nirvana


# class Fivesta:
#     members=3
#     albums=2
#     songs=6
#     listenings=470000
# fivesta=Fivesta