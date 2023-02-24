# # Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом
# # массиве), которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве,
# # затем N чисел - элементы массива. 
# # Затем число M - количество элементов во втором массиве. Затем элементы второго массива

# def diff(list_1, list_2):
#     list_3 =[]
#     for item in list_1:
#         if item not in list_2:
#             list_3.append(item)
#     return list_3

# len_array1 = int(input('Введите колличесвто элементов в первом массиве: '))
# import random
# list_1 = [random.randint(0, 20) for i in range(len_array1)]
# len_array2 = int(input('Введите колличество элементов во втором массиве: '))
# list_2 = [random.randint(0,20) for i in range(len_array2)]
# print(list_1, list_2)
# print(diff(list_1, list_2 ))

# # Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит
# # количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала 
# # вводится число N — количество элементов в массиве Далее записаны N чисел — элементы массива. Массив
# # состоит из целых чисел.
# # Ввод: 
# # 5 
# # 1 2 3 4 5 
# # Вывод:  0

# def search(list_1):
#     count = 0
#     for i in range(1, len(list_1)-1):
#         if list_1[i] > list_1[i+1] and list_1[i] > list_1[i-1]:
#             count+=1
#         i+=1
#     return count

# len_array = int(input('Введите количество элементов в массиве : '))
# import random 
# list_1 = [random.randint(0,20) for i in range(len_array)]
# print(list_1)
# print(search(list_1))

# # Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые
# # два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. Вводится список
# # чисел. Все числа списка находятся на разных строках.
# # Ввод: 1 2 3 2 3 
# # Вывод: 2
# def search_double(list_1):
#     count = 0
#     for i in range(len(list_1) - 1):
#         for j in range(i + 1, len(list_1)):
#             if list_1[i] == list_1[j]:
#                 count+=1
#     return count 

# n = int(input('Введите длину списка, и элементы для Enter: '))
# list_1 = list()
# for i in range(n):
#     n = int(input())
#     list_1.append(n)
# print(list_1)
# print(search_double(list_1))

# start_lst = [10, 10, 20, 20]
# count = 0
# for i in range(len(start_lst) - 1):
#     num_1 = start_lst[i]
#     for j in range(i + 1, len(start_lst)):
#         num_2 = start_lst[j]
#         if num_1 == num_2:
#             count += 1
# print(count)

# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, непревосходящее 10000. Программа должна вывести все
# пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод: 300
# Вывод: 220 284

# k = int(input('Введите число: '))
# def friendly_pair(k):
#     for i in range(1, k + 1):
#         sum = 0 
#         for j in range(1, k):
#             if i % j == 0:
#                 sum +=j
#         if sum <=i and sum <=j:
#             print(i, j) 
# print(friendly_pair(k))

k = int(input('Введите число:'))

def divisors_sum (n):
    sum = 0
    for i in range (1, n):
        if n % i == 0:
            sum += i
    return sum

def friendly_pair (n):
    for i in range (2, n + 1):
        if i <= n and divisors_sum (i) <= n:
            print(i, divisors_sum (i))
friendly_pair(k)