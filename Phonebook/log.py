from datetime import datetime

def log_cash(mod, result):
    path = 'Phonebook\log.txt'
    with open(path, 'a', encoding='utf-8') as file:
        file.write(f'Время: {datetime.now()}; Вид: {mod}; Данные: {result}\n')