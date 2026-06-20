import os
from utils import TextParser, is_valid_status
from models import ClassRoom, Student, Schedule, AttendanceRecord

class FileStorage:
    def __init__(self, data_folder):
        self.data_folder = data_folder
        self.classes_file = os.path.join(data_folder, "classes.txt")
        self.students_file = os.path.join(data_folder, "students.txt")
        self.schedules_file = os.path.join(data_folder, "schedules.txt")
        self.attendance_file = os.path.join(data_folder, "attendance.txt")

    def ensure_files(self):
        if not os.path.exists(self.data_folder):
            os.makedirs(self.data_folder)

        self.create_file_if_missing(self.classes_file)
        self.create_file_if_missing(self.students_file)
        self.create_file_if_missing(self.schedules_file)
        self.create_file_if_missing(self.attendance_file)

    def create_file_if_missing(self, file_path):
        if not os.path.exists(file_path):
            with open(file_path, "w", encoding="utf-8") as file:
                file.write("")

    def load_all(self, classes, students, schedules, attendance_records):
        self.ensure_files()
        self.load_classes(classes)
        self.load_students(students)
        self.load_schedules(schedules)
        self.load_attendance(attendance_records)

    def load_classes(self, classes):
        classes.clear()
        with open(self.classes_file, "r", encoding="utf-8") as file:
            for line in file:
                clean_line = line.strip()
                if clean_line != "":
                    class_id = TextParser.get_field(clean_line, 0).strip()
                    class_name = TextParser.get_field(clean_line, 1).strip()
                    if class_id != "" and class_name != "":
                        classes.append(ClassRoom(class_id, class_name))

    def load_students(self, students):
        students.clear()
        with open(self.students_file, "r", encoding="utf-8") as file:
            for line in file:
                clean_line = line.strip()
                if clean_line != "":
                    class_id = TextParser.get_field(clean_line, 0).strip()
                    student_id = TextParser.get_field(clean_line, 1).strip()
                    full_name = TextParser.get_field(clean_line, 2).strip()
                    if class_id != "" and student_id != "" and full_name != "":
                        students.append(Student(class_id, student_id, full_name))

    def load_schedules(self, schedules):
        schedules.clear()
        with open(self.schedules_file, "r", encoding="utf-8") as file:
            for line in file:
                clean_line = line.strip()
                if clean_line != "":
                    class_id = TextParser.get_field(clean_line, 0).strip()
                    weekday = TextParser.get_field(clean_line, 1).strip()
                    period = TextParser.get_field(clean_line, 2).strip()
                    room = TextParser.get_field(clean_line, 3).strip()
                    if class_id != "" and weekday != "" and period != "" and room != "":
                        schedules.append(Schedule(class_id, weekday, period, room))

    def load_attendance(self, attendance_records):
        attendance_records.clear()
        with open(self.attendance_file, "r", encoding="utf-8") as file:
            for line in file:
                clean_line = line.strip()
                if clean_line != "":
                    class_id = TextParser.get_field(clean_line, 0).strip()
                    date = TextParser.get_field(clean_line, 1).strip()
                    student_id = TextParser.get_field(clean_line, 2).strip()
                    status = TextParser.get_field(clean_line, 3).strip()
                    if class_id != "" and date != "" and student_id != "" and is_valid_status(status):
                        attendance_records.append(AttendanceRecord(class_id, date, student_id, status))

    def save_all(self, classes, students, schedules, attendance_records):
        self.ensure_files()
        self.save_classes(classes)
        self.save_students(students)
        self.save_schedules(schedules)
        self.save_attendance(attendance_records)

    def save_classes(self, classes):
        with open(self.classes_file, "w", encoding="utf-8") as file:
            current = classes.head
            while current is not None:
                file.write(current.data.to_file_line() + "\n")
                current = current.next

    def save_students(self, students):
        with open(self.students_file, "w", encoding="utf-8") as file:
            current = students.head
            while current is not None:
                file.write(current.data.to_file_line() + "\n")
                current = current.next

    def save_schedules(self, schedules):
        with open(self.schedules_file, "w", encoding="utf-8") as file:
            current = schedules.head
            while current is not None:
                file.write(current.data.to_file_line() + "\n")
                current = current.next

    def save_attendance(self, attendance_records):
        with open(self.attendance_file, "w", encoding="utf-8") as file:
            current = attendance_records.head
            while current is not None:
                file.write(current.data.to_file_line() + "\n")
                current = current.next
