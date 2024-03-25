from Domain.Note import Note

def run():
    is_running = True
    notes = []
    help()

    while (is_running):
        operator = input("Введите команду: ").lower()
        if operator == "add":
            buff_head = input("Введите тему: ")
            buff_body = input("Введите текст записки: ")
            buff_note = Note(buff_head, buff_body)
            notes.append(buff_note)
        elif operator == "del":
            count = 1
            if len(notes) == 0:
                print("Записи отсутвуют")
            else:
                for note in notes:
                    print(count, ")", note.to_string())
                    count = ++count
                index = int(input("Выберите номер записи: "))
                if index <= len(notes) or index > 0:
                    notes.pop(index-1)
                else:
                    print("Записи с таким номером нет")
        elif operator == "print":
            print()
            count = 1
            if(len(notes) == 0):
                print("Записи отсутвуют")
            for note in notes:
                print(count, ")",note.to_string())
                count = ++count
        elif operator == "help":
            help()
        elif operator == "exit":
            is_running = False
        else:
            print("Команда неверна")


def help():
    print("add - добавить запись\n"
          "del - удалить запись\n"
          "print - вывести все записи\n"
          "help - вывод всех команд\n"
          "exit - выход\n")


