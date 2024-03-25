from datetime import datetime


class Note:
    def __init__(self, head="String", body="String", time_stamp=datetime.now()):
        self.head = head
        self.body = body
        self.time_stamp = time_stamp


    def get_head(self):
        return self.head

    def get_body(self):
        return self.body

    def get_time_stamp(self):
        return self.time_stamp

    def set_head(self):
        self.head = self

    def set_body(self):
        self.body = self

    def set_time_stamp(self):
        self.time_stamp = self

    def to_string(self):
        return datetime.strftime(self.time_stamp, "%d/%m/%y %H:%M:%S"), self.head, self.body

