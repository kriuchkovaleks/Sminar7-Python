

def get_export_column(data):
    for i in data:
        with open('directory.txt', 'a', encoding='utf-8') as file:
            file.write(f'\n{i}\n')


def get_export_row(data):
    for i in data:
        with open('directory.txt', 'a', encoding='utf-8') as file:
            file.write(f'{i}, ')
