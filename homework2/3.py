# Задача №3:
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8

n = int(input('Число N = '))
numbers = []
num = 1
while num < n:
    numbers.append(num)
    num *= 2
print(numbers)
