# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке

# Ввод:
# пара-ра-рам рам-пам-папам па-ра-па-дам 
# Вывод:
# Парам пам-пам

# Вариант 1
a=input('введите стихотворение: ')

b=a.split()

res=list(map(lambda x: x.count('а'),b))

for i in range(len(res)-1): 
    if res[i]==res[i+1]: 
        print("Парам пам-пам")
    else: 
        print("Пам парам") 


# # Вариант 2
a=input('введите стихотворение: ')
b=a.split()

def sort(f,col): 
    return [f(x) for x in col]

list=sort(lambda x: x.count('а'),b)

def fin(f,col): 
    if len(f(col))==1: 
        print("Парам пам-пам") 
    else: 
        print("Пам парам")
         
fin(set,list) 
    

# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.

# Ввод:
# print_operation_table(lambda x, y: x * y) 

# Вывод: 
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36 


def print_operation_table(operation, num_rows=6,num_columns=6):
    
    for num_columns in range(1,num_columns+1):
    
        print(*[operation(num_rows,num_columns) for num_rows in range(1,num_rows+1)])
    
# Вызов
print_operation_table(lambda x, y: x * y)




