#Крестики-нолики 

# field=[0,1,2,3,4,5,6,7,8]

# def fieldPrint():
#     print(field[0]," ",field[1]," ",field[2])
#     print(field[3]," ",field[4]," ",field[5])
#     print(field[6]," ",field[7]," ",field[8])

# def checkWinCombination(field): 
#     if (field[0]==field[1]==field[2] or field[3]==field[4]==field[5] or field[6]==field[7]==field[8]
#     or field[0]==field[3]==field[6] or field[1]==field[4]==field[7] or field[2]==field[5]==field[8]  
#     or field[0]==field[4]==field[8] or field[2]==field[4]==field[6]):
#         return True
#     else: 
#         return False

# fieldPrint()

# count=0
# win=False
# while win==False:
            
#     print('your are next: ')
#     target=int(input())
#     field[target]="X" 

#     count+=1
#     print("Step",count)

#     if count>=5: 
#         win=checkWinCombination(field)
#         # print(checkWinCombination(field))
#         if win==True:
#             print('you win!') 
#             fieldPrint()
#             break         
#     fieldPrint()

#     print('comp go')
#     for i in range(0,8):
#         if field[i] !="X" and field[i] != "О":
#             field[i]="О"
#             break
#     count+=1
#     print("Step",count)

#     if count>=5: 
#         win=checkWinCombination(field)
#         # print(checkWinCombination(field)) 
#         if win==True: 
#             print('Comp win!')
#             fieldPrint()
#             break

#     fieldPrint()

# Задача 30: 
# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: Аn = A1+(n-1)*d.
# Каждое число вводится с новой строки.

# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

# A1=int(input('введите первый элемент: '))
# d=int(input('введите разность: '))
# k=int(input('введите количество элементов: '))

# A=[]
# A.append(A1)

# n=2

# while n<k+1: 
#     An=A1+(n-1)*d
#     n+=1
#     A.append(An)
# print(*A)

# Задача 32:
# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не 
# меньше заданного минимума и не больше заданного максимума).
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

from random import randint

n=int(input('введите количество символов: '))
a=[]
for i in range(n): 
    a.append(randint(-5,10))
print(a)

min=int(input('введите минимум диапазона: '))
max=int(input('введите максимум диапазона: '))

b=[]
for i in range(n):
 
    if a[i]>=min and a[i]<=max:
        b.append(i)

if len(b)==0: 
    print('нет значений которые входят в заданный диапазон')
else: 
    print(b)



