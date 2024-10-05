#1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
def hw_1():
    ls = []
    for i in a:
        if i % 2==0:
            ls.append(i)
    print(ls)
hw_1()




#3
x = [4, 7, 8, 24, 12, 2, 1]
max_num = 0
for i in x:
    if i > max_num:
        max_num = i
print(max_num)

def num2():
    max_num=0
    for i in x:
        if i>max_num:
            max_num = i
    print(max_num)
num2()




