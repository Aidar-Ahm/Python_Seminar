# #1. Дан список чисел. Определите, сколько в нем встречается различных чисел. [1, 2, 2, 3, 5, 6] -> 5 

# list_1 = list()
# for i in range(5):
#     n = int(input())
#     list_1.append(n)
# print(list_1)
# print(f'кооличество разных чисел {len(set(list_1))}')

# ##2. Дана последовательность из N целых чисел и число K.  Необходимо сдвинуть всю последовательность 
# ##(сдвиг - циклический) на K элементов вправо,
# ## K – положительное число. [1, 2, 3, 4, 5] 3 -> [3, 4, 5, 1, 2] 
# list_1 = [1,2,3,4,5,6]
# k = int(input('Введите число К: '))
# k = -(k%len(list_1))
# list_2 =[]
# for i in range(len(list_1)):
#     list_2.append(list_1[k])
#     k += 1
# print(list_2)

# 3. Напишите программу для печати всех уникальных значений в словаре.
#  {     1: 'V',     4: 'C',     'ew': 'C' } -> V, C 
dict_1 = {1: 'V',     4: 'C',     'ew': 'C'}
print(*set(dict_1.values()))

# # Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива, 
# # больших предыдущего (элемента с предыдущим номером)
# # [6, 9, 3, 6, 87, 1, 3]
# list_1 = [1, 2, 3, 2, 1, 0]
# count = 0
# for i in range(len(list_1)-1):
#     if list_1[i+1] > list_1[i]:
#         count +=1
# print(f'Колличество цифр больших предидущего {count}')