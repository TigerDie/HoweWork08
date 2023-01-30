journal_class = {}

def get_journal() -> dict:
    return journal_class


def read_db(path: str):
    with open(path, 'r', encoding='UTF-8') as file:
        data_lessons = file.readlines()
        for line in data_lessons:
            lessons = line.strip().split(';')
            lesson = lessons[0]
            student_marks = lessons[1].split(',')
            student = []
            marks = []
            for item in student_marks:
                pupil_marks = item.split(':')
                student.append(pupil_marks[0])
                marks.append(pupil_marks[1].split())
            for i, value in enumerate(marks):
                marks[i] = list(map(int, value))
            journal_class[lesson] = dict(zip(student, marks))
    return journal_class

def add_mark(journal: dict, mark: int, lesson: str, name: str, path: str) -> dict:
    journal[lesson][name].append(mark)
    save_changes(journal, path)
    return journal_class

def check_name(journal: dict, name: str):
    flag = False
    for item in journal.values():
        for key in item.keys():
            if name == key:
                flag = True
    return flag

def check_lesson(journal: dict, lesson: str) -> bool:
    flag = False
    for key in journal.keys():
        if lesson == key:
            flag = True
    return flag

def check_info(journal: dict, lesson: str, name: str) -> bool:
    return check_name(journal, name) and check_lesson(journal, lesson)

def save_changes(journal: dict, path: str):
    file_string = ''
    for i in journal.keys():
        file_string += i + ';'
        for j in journal[i].keys():
            file_string += j + ':'
            for k in range(len(journal[i][j])):
                file_string += ' ' + str(journal[i][j][k])
            file_string = file_string + ','
        file_string = file_string[:-1] + '\n'
    file_string = file_string[:-1]
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(file_string)