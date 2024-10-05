# students = {"Nurbek", "Ulukman", "Kumushay", "Rustam", "Gulzina","Abdulatif"}


# name = input("input student's name: ")
# if name in students:
#     print("Ученик ITC")
# else:
#     "Не наш ученик"
#     print(students)



# a=int(input("Введите число: "))
# b=''
# for i in range(a+1):
#     b =(str(i) + '')*i
#     print(b)


# Напишите класс Python, чтобы перевернуть строку слово за словом
# ввод hello.py
# ожидание py.hello

# music.mp3
# mp3.music

# im.jpeg
# jpeg.im

# a="im.jpeg"
# a=a.split(".")
# b=""
# b=b+a[1]+"."+a[0]
# print(b)



course =[1, 5, 6, 1, 8, 4, 4, 5, 1]
d={}
count = 0 
for i in course:
     if i == 1:
          count+=1
d[1]=count
count = 0 
for i in course:
     if i ==5:
          count+=1
d[5]=count
count = 0 
for i in course:
     if i == 6:
          count+=1
d[6]=count
count = 0 
for i in course:
     if i == 8:
          count+=1
d[8]=count
count = 0 
for i in course:
     if i == 4:
          count+=1
d[4]=count
count = 0 
print(count)
print(d)



# a = int(input("Введите четное число"))
# if a % 2==0:
#      b=int(input("6+9+6*9:"))
#      if b==69:
#           print("Красавчик!!!")
#      else:
#           print("Иди в 3-класс!")

# else:
#      print("Иди в 3-класс!")


