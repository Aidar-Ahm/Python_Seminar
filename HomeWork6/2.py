# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

def fill_array(n):
    print('Введите элементы')
    list_1 = list()
    for i in range(n):
        a = int(input())
        list_1.append(a)    
    return(list_1)

def show_index(list_1, min, max):
    list_3= list()
    for i in range(len(list_1)):
        if list_1[i] > min and list_1[i] < max:
            list_3.append(i)
    print(list_3)            

n = int(input('колличество элементов списка: '))
min = int(input('Минимум: '))
max = int(input('Максимум: '))
show_index(fill_array(n), min, max)
