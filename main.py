from quize import games
from account import bank_account
from work_with_file import create, delete, copy,files, dir
import os
import sys

while True:
    print('1. Создать папку')
    print('2. Удалить (файл/папку)')
    print('3. Копировать (файл/папку)')
    print('4. Просмотр содержимого рабочей директории')
    print('5. Посмотреть только папки')
    print('6. Посмотреть только файлы')
    print('7. Просмотр информации об операционной системе')
    print('8. Создатель программы')
    print('9. Играть в викторину')
    print('10. Мой банковский счет')
    print('11. Cмена рабочей директории (*необязательный пункт)')
    print('12. Выход')

    choice = input('Выберите пункт меню ')
    if choice == '1':       # Создать папку
        create()
    elif choice == '2':     # Удалить (файл/папку)
        delete()
    elif choice == '3':     # Копировать (файл/папку)
        copy()
    elif choice == '4':     # Просмотр содержимого рабочей директории
        print("Содержимое рабочей директории:")
        for name in os.listdir():
            print(name)
    elif choice == '5':    # Посмотреть только папки
        print("Cписок файлов", dir())
    elif choice == '6':    # Посмотреть только файлы
        print("Cписок файлов", files())
    elif choice == '7':    # Просмотр информации об операционной системе
        print("Операционной система", sys.platform)
    elif choice == '8':    # Создатель программы
        print('Автор программы: Мария Гаврилова')
    elif choice == '9': # Играть в викторину
        games()
    elif choice == '10': # Мой банковский счет
        bank_account()
    # elif choice == '11': # Cмена рабочей директории (*необязательный пункт)
    #     os.chdir(path)
    elif choice == '12':
        break
    else:
        print('Неверный пункт меню')
    print()