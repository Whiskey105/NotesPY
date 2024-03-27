import Domain.Note
from csv import DictReader, DictWriter
from os.path import exists

"""def write_file(array, mode):
    file = open("notes.csv", mode='w', encoding='utf-8')
    file.seek(0)
    file.close()
    file = open("notes.csv", mode=mode, encoding='utf-8')
    for note in array:
        file.write(Domain.Note.Note.to_string(note))
        file.write('\n')
    file.close()"""


"""def read_file():
    try:
        array = []
        file = open("notes.csv", "r", encoding='utf-8')
        notes = file.read().strip().split('\n')
        for note in notes:
            sptited_line = note.split(';')
            note = Domain.Note.Note(id=sptited_line[0], time_stamp=sptited_line[1], head=sptited_line[2], body=sptited_line[3])
            array.append(note)
    except Exception:
        print("Журнал пуст")
    finally:
        return array"""

def write_file(file_name, notes):

    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['id','дата','тема','заметка'])
        f_writer.writeheader()
        f_writer.writerows(notes)

def create_file(file_name):
    with open(file_name, 'w', encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['id','дата','тема','заметка'])
        f_writer.writeheader()

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)

def print_file(file_name):
    res = read_file(file_name)
    row = 1
    for r in res:
        print(row, r)
        row += 1