# a=5
# lst=[]
# for i in range(a):
#     for y in range(i):
#         lst.append(i)
# print(*lst[0:a])


# """Классы"""
# class Douch:
#     muka = 400
#     salt = 15
#     eggs = 2
#     butter = 50
#     raz = 15
#     sugar = 100
#     lemon = 1

#     def mix(self):
#         print("We must to mix all recepts")
#     def add_muka(self):
#         self.muka = self.muka + 50
#         print("В конце получилось",self.muka,"гр")
#     def add_eggs(self,count):
#         self.eggs=self.eggs +count    
#         print("Колл-во яиц",self.eggs)
# pie=Douch()
# print("Колличевство сахара",pie.sugar,"гр")
# print("Колличевство соли",pie.salt,"гр")
# print("Колличевство муки",pie.muka,"гр")
# print("Колличевство яйца",pie.eggs,"гр")
# print("Колличевство сл.масла",pie.butter,"гр")
# print("Колличевство разрыхнителя",pie.raz,"гр")
# print("Колличевство лимона",pie.lemon,"гр")
# pie.add_muka()
# pie.add_muka()
# pie.add_eggs(2)


# class Notebook:
#     CPU ="Core i5"
#     RAM =8
#     graphics_card ="VGA Card PALIT GeForce RTX3090 GAMEROCK 24G GDDR6X 384bit,HDMI+3DP (NED3090T19SB-1021G) NON-LHR"
#     HDD=240
#     motherboard=True
#     Screen_size=16.3
#     def my_n(self):
#         print("Процессор:",self.CPU)
#         print("Оперативная память:",self.RAM)
#         print("Видео карта:",self.graphics_card)
#         print("Жесткий диск:",self.HDD)
#         print("Материнская плата:",self.motherboard)
#         print("Размер:",self.Screen_size)
# lenovo570G = Notebook()
# lenovo570G.my_n()

# class Human:
#     name=None
#     age=None
#     def __init__(self, name, age):
#         self.name1=name
#         self.age1=age
#     def deskription(self):
#         print("Имя",self.name1)
#         print("Возраст",self.age1)
# human=Human("Асан",25)
# human.deskription()

# human2=Human("Кумушай",17)
# human2.deskription()

# class Cat:
#     name="Матроскин"
#     color ="black"
#     def my_cat(self):
#         print("Имя:",self.name)
#         print("Цвет:",self.color)
# Matroskin = Cat()
# Matroskin.my_cat()


class Cat:
    name=None
    age=None
    def __init__(self, name, color):
        self.name1=name
        self.color1=color
    def deskription(self):
        print("Имя",self.name1)
        print("Цвет",self.color1)
cat=Cat("Матроскин","Black")
cat.deskription()
