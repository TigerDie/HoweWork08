import sys
import model
import view
path = ''

def input_teacher(command: int):
    match command:
        case 1:
            view.show_list_student(model.get_journal())
        case 2:
            view.show_journal(model.get_journal())
        case 3:
            lesson = view.get_lesson()
            if model.check_lesson(model.get_journal(), lesson):
                view.show_progress_lesson(model.get_journal(), lesson)
            else:
                view.show_message()
                print('Информация не найдена! ')
        case 4:
            control_knowledge()
        case 5:
            sys.exit()

def start():
    global path
    view.main_menu()
    access = view.choice_access()
    path = view.choice_class()
    model.read_db(path)
    if access == 1:
        while True:
            command = view.command_teacher()
            input_teacher(command)

def control_knowledge():
    lesson = view.get_lesson()
    if model.check_lesson(model.get_journal(), lesson):
        view.show_message('Кто будет отвечать?')
        name = view.get_name()
        if model.check_name(model.get_journal(), name):
            mark = view.control()
            model.add_mark(model.get_journal(), mark, lesson, name, path)
            view.show_student_lesson(model.get_journal(), name, lesson)
        else:
            view.show_message()
            print('Информация не найдена! ')
    else:
        view.show_message()
        print('Информация не найдена! ')