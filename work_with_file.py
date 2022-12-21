import os
import shutil

def create():
    while True:
        name = input('Какую папку создать? Введите название: ')
    # проверка на существование
        if not os.path.exists(f'{name}'):
            # сздать папку передаем путь
            os.mkdir(f'{name}')
            break
        else:
            print('Папка с таким именем существует')


def delete():
    while True:
        name = input('Какую папку удалить? Введите название ')
        # проверка на существование
        if os.path.exists(f'{name}'):
            # удалить папку
            os.rmdir(f'{name}')
            break
        else:
            print('Папки/файла с таким именем не существует')
            print()


def copy():
    name = input('Какую папку скопировать? Введите название ')
# проверка на существование
    if os.path.exists(f'{name}'):
        # копировать
        shutil.copy(f'{name}',f'{name}_copy.py')
    else:
        print('Папки/файла с таким именем не существует')
        print()

def files():   # os.path.isfile(path) - является ли путь файлом
    dirPath = os.getcwd()
    result = [f for f in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, f))]
    print(result)

def dir():    #os.path.isdir(path) - является ли путь директорией.
    dirPath = os.getcwd()
    result = [f for f in os.listdir(dirPath) if os.path.isdir(os.path.join(dirPath, f))]
    print(result)

# def delete():
#     shutil.copy('famous_info.py', 'famous_info_copy.py')
#


if __name__ == '__main__':
    copy()
    # delete()
    # files()
    # dir()