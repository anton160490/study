# Задача 26
# Напишите программу, которая на вход принимаетдва числа A и B, 
# и возводит число А в целую степень B спомощью рекурсии.

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

A=int(input('введите число А: '))
B=int(input('введите число B: '))

def func(A,B): 
    if B==0: 
        return 1
    return A*func(A,B-1)
print(func(A,B))

# Задача 28:
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
    
def  sum(a,b):
    if b==0: 
        return a
    return sum(a+1,b-1)
print(sum(12,7))       
    
        