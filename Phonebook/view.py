def inp_mod():
    mod = input('Введите режим работы (импорт или экспорт): ')
    mod = mod.lower()
    return mod


def inp_import():
    surname = input('Введите фамилию для поиска данных: ')
    return surname


def inp_export():
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    phone = input('Введите телефон: ')
    text_comment = input('Введите комментарий: ')
    return surname, name, phone, text_comment


def view_import(result):
    print(f'По введенным  данным найдены записи: {result}')


def view_export():
    print('Данные сохранены.')