documents = [
{'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
{'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
{'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
'1': ['2207 876234', '11-2'],
'2': ['10006'],
'3': []
}
def owner(number_doc):
    """
    Функция возвращает по номеру документа данные о его владельце
    """
    owner_name = ''
    for row in documents:
        if row['number'] == number_doc:
            owner_name = 'Владелец документа: ' + row['name']
    if owner_name == '':
        owner_name = 'Документ не найден в базе'
    return owner_name
def main():
    """
    Основная функция автоматизации работы секретаря
    """
    a = 0
    while a < 1:
        command_input=input('Введите команду: \n')
        if command_input == 'p':
            number_input=input('Введите номер документа: \n')
            print(owner(number_input))
          else:
            print('Нет такой команды')
main()