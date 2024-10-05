# Задание на хакатон: создать Банкомат с балансом, паролем, пополнением и снятием баланса.
# blik_Method(self):
#         print(f"Пользователь:{self.name}")
#     def _prot
# У вас долно быть:
# 1. Пароль, пинкод, при вводе которого он проверяется с настоящим пинкодом и при вводе неправильного, он спрашивает его заного, пока не вводится настоящий.
# 2. Баланс, тоесть, у вас должен быть изначальный баланс, и вы должны в ходе выполнения работы банкомата, обменивать баланс на другие валюты (USD, EU, KZT, KGS)
# 3. Курс t(input("Введите четное чвалюты, 1 USD = 84 KGS, 1 EU = 95 KGS, 1 KZT = 0.006 KGS
# dMethod(self):.__password=__
#      
#         print(f"Пользователь:{self.name}, \nid: {self._id}")
#     def __privateMethod(self):
#         prin
# class Bankomat:
#     def __init__(self,name,_id,__password,moneys):
#         self.som=moneys
#         self.name = name
#         self._idpassword
#     def puektet(f"Пользователь:{self.name}, \nid: {self._id} \nпороль:{self.__password} \nУ вас на карте:{self.som}сомов")
# bank = Bankomat("Alex","1234567","qwerty54321","84000")
# bank.publik_Method
# bank._protektedMethod
# bank._Bankomat__privateMethod()
# a = inисло"))
# if a % 2==0:=_id
#         selfb=int(input("6+9+6*9:"))
#      if b==69:
#           print("Красавчик!!!")
#      else:
#           print("Иди в 3-класс!")

# else:
#      print("Иди в 3-класс!")

while True: 
    som=1
    ru=1.16
    usd=84
    eu=95
    kzt=5.12
    s=int(input("Введите пин-код: "))
    if s== 1234: 
        summ=10000
        a = int(input("Если хотите вывести деньги введите 1:\nЕсли хотите пополнить нажмите 2:\nЕсли хотите узнать баланс введите 3:"))
        if a==1:
            y=int(input("Выберите валюту:\n1-Доллар:\n2-Евро:\n3-Тенге:\n4-Cом:"))
            if y==1:
                p=summ/usd
                print(f" Ваш баланс {p} доллар")
                i=int(input("Сколько хотите выести:"))
                if i < p:
                    print("У вас не достаточно средств")
                print(f"У вас осталось:{p-i} долларов")
            elif y==2:
                g=summ/eu
                print(f" Ваш баланс {g} евро")
                v=int(input("Сколько хотите выести:"))
                print(f"У вас осталось:{g-v}euro")
            elif y==3:
                o=summ*kzt
                print(f" Ваш баланс {o} тенге")
                q=int(input("Сколько хотите выести:"))
                print(f"У вас осталось:{o-q}тенге")
            elif y==4:
                print(f"Ваш баланс {summ} сом")
                w=int(input("Сколько хотите выести:"))
                print(f"У вас осталось:{summ-w}сом")
            else:
                print("Выбрана неверная операция")
        elif a==2:
            u=int(input("На какую сумму хотите пополнить:"))
            print(f"Ваш баланс пополнен на сумму:{u}Текуший баланс:{summ+u}")
        elif a==3:
            print(f"Ваш баланс:{summ}сомов")
        elif a==4:
            print(f"Доллар|USD {usd}\nЕвро|EURO {eu}\nТенге|KZT {kzt}\nРубль|RU {ru}")
        else:
            print("Выбрана неверная операция")
    else:
        s != 1234
        print("Пин-код не верный")
    
