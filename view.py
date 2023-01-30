num_class = ''

def main_menu():
    print('\n\tЖурнал успеваемости учеников\t\n')
    menu_list = ['Раздел для учителей']
    for i, item in enumerate(menu_list):
        print(f'\t{i + 1}. {item}')

def choice_access() -> int:
    while True:
        try:
            access = int(input('\nВведите номер: '))
            if access not in [1]:
                print('Введите 1!')
            elif access in [1]:
                return access
        except ValueError:
            print('Ахтунг! Введите число 1')

def choice_class() -> str:
    global num_class
    while True:
        try:
            class_num = input('\nВведите класс: ')
            if class_num.lower() not in ['7а']:
                print('Доступен класс 7А')
            elif class_num.lower() in ['7а']:
                path = class_num.upper() + '.txt'
                num_class = class_num
                return path
        except ValueError:
            print('Ахтунг! Введите число 1')

def show_journal(journal: dict):
    print(f'\nОценки учеников в классе:\n')
    for key in journal.keys():
        print(f'{key}:')
        j = 0
        for i, item in journal[key].items():
            j += 1
            print(f'\t{j}. {i}: ', end=' ')
            print(*item)
        print()

def get_name() -> str:
    name = input('Введите имя и фамилию ученика: ')
    print()
    return name.title()

def get_lesson() -> str:
    lesson = input('Введите название предмета: ')
    print()
    return lesson.capitalize().strip()

def show_message(text: str):
    print(text)

def show_student_lessons(journal: dict, name: str):
    print(f'Ученик класса 7А {name}')
    for key in journal.keys():
        print(f'\t{key}:', end=' ')
        for i, item in journal[key].items():
            if i == name:
                print(*item)

def show_student_lesson(journal: dict, name: str, lesson: str):
    print(f'Ученик класса 7А {name}')
    print(f'\t{lesson}: ', end=' ')
    print(*journal[lesson][name])

def menu_teacher():
    menu_list = [
        'Список всех учеников',
        'Оценки всех учеников по всем предметам',
        'Оценки учеников по предмету',
        'Оценки на уроке',
        'Выход',
                ]
    print('\n* Главное меню *')
    for i, item in enumerate(menu_list):
        print(f'\t{i + 1}. {item}')

def command_teacher() -> int:
    while True:
        try:
            menu_teacher()
            command = int(input('\nВведите номер команды: '))
            if command < 1 or command > 5:
                print('Введите номер команды от 1 до 5!')
            else:
                return command
        except ValueError:
            print('Ахтунг! Введите число 1 или 5.')

def show_list_student(journal: dict):
    print(f'\nСписок всех учеников в 7А классе: ')
    for item in journal.values():
        i = 0
        for key in item.keys():
            i += 1
            print(f'\t{i}. {key}')
        break

def show_progress_lesson(journal: dict, lesson: str):
    print(f'\nОценки учеников 7А класса')
    print(f'Предмет: {lesson.lower()}\n')
    i = 0
    for key, value in journal[lesson].items():
        i += 1
        print(f'\t{i}. {key}: ', end=' ')
        print(*value)

def control() -> int:
    while True:
        try:
            mark = int(input('Введите полученную отметку: '))
            if mark not in [1, 2, 3, 4, 5]:
                print('Введите отметку от 1 до 5.')
            elif mark in [1, 2, 3, 4, 5]:
                return mark
        except ValueError:
            print('Такой оценки не может быть!')