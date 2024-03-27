import Domain.Note
import File
from Domain.Note import Note
from os.path import exists\

def run():
    is_running = True
    notes = []
    help()

    file_name = "notes.csv"
    if not exists(file_name):
        File.create_file(file_name)

    notes = File.read_file(file_name)

    while (is_running):
        operator = input("Введите команду: ").lower()
        if operator == "add":
            """buff_head = input("Введите тему: ")
            buff_body = input("Введите текст записки: ")
            buff_note = Domain.Note.Note(head=buff_head, body=buff_body)
            obj = {'id' : buff_note.get_id() ,'дата' : buff_note.get_time_stamp(),'тема' : buff_note.get_head(),'заметка' : buff_note.get_body()}
            notes.append(obj)"""
            add_note(notes)
            File.write_file(file_name=file_name, notes=notes)
        elif operator == "del":
            File.print_file(file_name)
            count = 1
            if len(notes) == 0:
                print("Записи отсутвуют")
            else:
                index = int(input("Выберите номер записи: "))
                if index <= len(notes) or index > 0:
                    notes.pop(index-1)
                    File.write_file(file_name=file_name, notes=notes)
                else:
                    print("Записи с таким номером нет")
        elif operator == "print":
            File.print_file(file_name)
        elif operator == "help":
            help()
        elif operator == "change":
            File.print_file(file_name)
            change_note(notes)
            File.write_file(file_name=file_name, notes=notes)
        elif operator == "exit":
            is_running = False
        else:
            print("Команда неверна")

def add_note(notes):
    buff_head = input("Введите тему: ")
    buff_body = input("Введите текст записки: ")
    buff_note = Domain.Note.Note(head=buff_head, body=buff_body)
    obj = {'id': buff_note.get_id(), 'дата': buff_note.get_time_stamp(), 'тема': buff_note.get_head(),
           'заметка': buff_note.get_body()}
    notes.append(obj)

def change_note(notes):
    if len(notes) == 0:
        print("Записи отсутвуют")
    else:
        index = int(input("Выберите номер записи: "))
        if index <= len(notes) or index > 0:
            notes.pop(index - 1)
            buff_head = input("Введите новую тему: ")
            buff_body = input("Введите новый текст записки: ")
            buff_note = Domain.Note.Note(head=buff_head, body=buff_body)
            obj = {'id': buff_note.get_id(), 'дата': buff_note.get_time_stamp(), 'тема': buff_note.get_head(),
                   'заметка': buff_note.get_body()}
            notes.append(obj)
        else:
            print("Записи с таким номером нет")


def help():
    print("add - добавить запись\n"
          "del - удалить запись\n"
          "print - вывести все записи\n"
          "change - изменить запись\n"
          "help - вывод всех команд\n"
          "exit - выход\n")


