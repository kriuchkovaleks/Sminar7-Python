

def view_data(data):
    return print(data)

def get_library_row():
    library = []
    library.append(input('Введите фамилию:'))
    library.append(input('Введите имя:'))
    library.append(input('Введите телефон:'))
    library.append(';')
    return library


def get_library_column():
    library = []
    library.append(input('Введите фамилию:'))
    library.append(input('Введите имя:'))
    library.append(input('Введите телефон:'))
    return library
    


def export_type():
    print('Выбирете вид фоматирования:\
        1. Строка   2. Столбец')
    exp_type = input()
    return exp_type
    