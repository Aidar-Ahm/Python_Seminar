# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, 
# номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной
# Добавить контакт

import os

base = r'C:\python_sem\seminar8\base.txt'

def append_contact(base):
    contact = input('Введите контакт в формате ФИО номер телефона:')
    with open(base, 'a', encoding='utf-8') as f:
        f.write(f'\n{contact}')
    print('Контакт добавлен')

def read_file(base):
    with open(base, 'r', encoding='utf-8') as f:
        print(f.read())

def search_contact(base):
    search = input('Введите информацию для поиска(фамилию, имя, отчество, номер телефона):')
    with open(base, 'r', encoding='utf-8') as f:
        for line in f:
            if search in line:
                print(line)

def user_interface():
    print('Добро пожаловать! \n1)Вывести весь справочник \n2)Добавить контакт \n3)Найти контакт')
    while (input1 := int(input('Выберите действие (Для выхода нажмите 0): '))) != 0:
        if input1 == 1: 
            read_file(base)
        elif input1 == 2: 
            append_contact(base)
        elif input1 == 3:
            search_contact(base)

        else:
            print('Некоректный ввод')

user_interface()