# Задача 2
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# 2 2
# 4

def sum(a, b : int):
    if a == 1 and b == 1:
        return a + b
    if a == 1: 
        return a + sum(a, b-1)
    if b == 1:
        return b + sum(a-1, b)
    return sum(1,1) + sum(a-1, b-1)
a = int(input('a = '))
b = int(input('b = '))
print(sum(a, b))