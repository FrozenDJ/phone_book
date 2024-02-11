"""
Создать телефонный справочник с возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые 
должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной
    записи(Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной

"""

from csv import DictReader, DictWriter
from os.path import exists
class LenNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt

def get_info():
    first_name = 'Ivan'
    last_name = "Ivanov"
    is_valid_number = False
    while not is_valid_number:
        try:
            phone_number = input('Введите номер: ')
            if len(str(phone_number)) != 6:
                raise LenNumberError('Некорректная длина')
            else:
                is_valid_number = True
        except ValueError:
            print('Неверный номер!')
            continue
        except LenNumberError as err:
            print(err)
            continue
    return [first_name, last_name, phone_number]

def create_file(file_name):
    with open(file_name, 'w', encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Номер телефона'])
        f_writer.writeheader()

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)
    
def write_file(file_name):
    result = read_file(file_name)
    user_data = get_info()
    for item in result:
        print(item['Номер телефона'], str(user_data[2]))
        if item['Номер телефона'] == str(user_data[2]):
            print('Такой пользователь уже существует')
            return
    obj = {'Имя': user_data[0], 'Фамилия': user_data[1], 'Номер телефона': user_data[2]}
    result.append(obj)
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Номер телефона'])
        f_writer.writeheader()
        f_writer.writerows(result)

def main():
    file_name = 'phone_csv'
    
    while True:
        command = input("Введите команду: ")
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name)
        elif command == 'r':
            if not exists(file_name):
                print('Файла не существует. Создайте файл')
                continue
            print(*read_file(file_name))
        elif command == 'c':
            pass

main()