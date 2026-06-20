class ClassRoom:
    def __init__(self, class_id, class_name):
        self.class_id = class_id
        self.class_name = class_name

    def to_file_line(self):
        return self.class_id + "|" + self.class_name

class Student:
    def __init__(self, class_id, student_id, full_name):
        self.class_id = class_id
        self.student_id = student_id
        self.full_name = full_name

    def to_file_line(self):
        return self.class_id + "|" + self.student_id + "|" + self.full_name

class Schedule:
    def __init__(self, class_id, weekday, period, room):
        self.class_id = class_id
        self.weekday = weekday
        self.period = period
        self.room = room

    def to_file_line(self):
        return self.class_id + "|" + self.weekday + "|" + self.period + "|" + self.room

class AttendanceRecord:
    def __init__(self, class_id, date, student_id, status):
        self.class_id = class_id
        self.date = date
        self.student_id = student_id
        self.status = status

    def to_file_line(self):
        return self.class_id + "|" + self.date + "|" + self.student_id + "|" + self.status

class AbsenceReportItem:
    def __init__(self, student, total_sessions, absence_count, absence_rate):
        self.student = student
        self.total_sessions = total_sessions
        self.absence_count = absence_count
        self.absence_rate = absence_rate
