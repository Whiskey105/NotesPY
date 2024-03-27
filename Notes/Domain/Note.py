from datetime import datetime
import uuid


class Note:
    def __init__(self, head="String", body="String", id=str(uuid.uuid4())[0:3], time_stamp=datetime.strftime(datetime.now(), "%d/%m/%y %H:%M:%S")):
        self.id = id
        self.head = head
        self.body = body
        self.time_stamp = time_stamp

    def get_id(self):
        return self.id

    def get_head(self):
        return self.head

    def get_body(self):
        return self.body

    def get_time_stamp(self):
        return self.time_stamp

    def set_id(self):
        self.id = self

    def set_head(self):
        self.head = self

    def set_body(self):
        self.body = self

    def set_time_stamp(self):
        self.time_stamp = self

    def to_string(self):
        return self.id + ';' + self.time_stamp + ';' + self.head + ';' + self.body

    def map_note(note):
        return '\nID: ' + note.id + '\n' + 'Название: ' + note.head + '\n' + 'Описание: ' + note.body + '\n' + 'Дата публикации: ' + note.time_stamp