#Problem1:
# Напишите функцию которая принимает *args и *kwargs которые принимают str и найдите длину всех значении
def func(*text, **second_t):
    p = len(text)
    pr = len(second_t)
    print(p+pr)
func('MDior', pp = 'Will')
#Problem2:
# С помошью условного оператора напишите код который принимет имя человека и проверяет если совпадает с именем в переменой naame то ввыведите "Right" иначе ввыедите "Повтори еще раз"


# Problem3
#с помощью тернарного оператора вывести сумму,произведения,разность
# lts2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

# Problem4
#Cделать калькулятор с выбором операция если пользователь ввел знак, который не является знаком арифметической операции то вывести сообщение о некорректном вводе необходимо проверить не является ли нулем второе число. Если это так, то сообщить о невозможности деления

# Problem5
#C помощью list comprehenstion операций вывести в списке нечетные числа
lts = [1,2,3,4,5,7,8,32,55, 32]
