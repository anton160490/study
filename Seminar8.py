# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию,
# и Вы должны реализовать функционал для изменения и удаления данных

import os

def selectAllReadPhoneNumber():
    phoneBook=readData('C:/Users/79852/Documents/Антон/file.txt')
    for i in phoneBook:
        print(i)

def readData(fileName):
    with open(fileName) as f: 
        phoneBook=[]
        for line in f:
            phoneBook.append(line.split(','))
        return phoneBook
    
def writeData(fileName, phoneBook):

    with open(fileName,'w') as data:
        for i in phoneBook:
            data.write(','.join(i))
    print("Data added and saved")
    print(phoneBook)

def addPerson(): 
    phoneBook=readData("C:/Users/79852/Documents/Антон/file.txt")
    print("Entered data")
    number=str(len(phoneBook)+1)
    surname=str(input("Entered surname:"))
    nameFirst=str(input("Entered first name:"))
    nameSecond=str(input("Entered second name:"))
    phoneNumber=str(input("Entered telephone number:"))
    phoneBook.append([number,surname,nameFirst,nameSecond,phoneNumber+'\n'])
    writeData("C:/Users/79852/Documents/Антон/file.txt",phoneBook)

def select():
    phoneBook=readData("C:/Users/79852/Documents/Антон/file.txt")

    while True:
        name=str(input("enter something to search for or 'q' for exit:\n"))
        if name=="q": 
            break
        n=0
        for i in phoneBook:
            if name in i:
                print(i) 
                n+=1
               
        if n==0:
            print('not found')

    
def EditOfDelete(): 
    phoneBook=readData("C:/Users/79852/Documents/Антон/file.txt")
    while True:
        name=str(input("enter something to search or 'q' for exit: \n"))
        if name=='q':
            return

        a=0
        for i in phoneBook: 
          
            if name in i:
                a+=1
                print(i)

                while True:
                    print("enter 'e' to change the line,'d' to delete or 'q' to exit:\n")
                    choice=str(input())
                    if choice=='e':
                        print(''' Enter the field to change: 
                                        \n [1] -- surname
                                        \n [2] -- nameFirst
                                        \n [3] -- nameSecond
                                        \n [4] -- PhoneNumber''')
                        field=int(input('Enter number:\n'))
                        if field==1:
                            print("Entered surname:")
                            i[1]=str(input())
                            print(i)
                        elif field==2:
                            print('Entered nameFirst:')
                            i[2]=str(input())
                            print(i)
                        elif field==3:
                            print('Entered nameSecond:')
                            i[3]=str(input())
                            print(i)
                        elif field==4:
                            print('Entered PhoneNumber:')
                            i[4]=str(input())
                            print(i)
                        writeData("C:/Users/79852/Documents/Антон/file.txt",phoneBook)  
                    elif choice=='d':
                        DeleteData(i,phoneBook)
                    elif choice=='q':
                        break                                                        
        if a==0:
            print('not found, please re-enter')
        
def DeleteData(i,phoneBook):
    phoneBook.remove(i)
    writeData("C:/Users/79852/Documents/Антон/file.txt",phoneBook)
 
clear=lambda: os.system('cls')
clear()

while True:

    print('''Hello, user 
        \n [1]--press for SHOW ALL 
        \n [2] --press for SELECT
        \n [3] --press for ADD DATA
        \n [4] --press for edit or delete DATA''')

    enteredNum=int(input())
    try:
        if enteredNum == 1:
            selectAllReadPhoneNumber()
        elif enteredNum == 2:
            select()
        elif enteredNum == 3:
            addPerson()
        elif enteredNum == 4:
            EditOfDelete()
        else:
            print("Your number out of range. Try again")
    except: 
        print("You entered something, but it's not number")
