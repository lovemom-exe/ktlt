from models import ClassRoom, Student, Schedule, AttendanceRecord, AbsenceReportItem
from utils import LinkedList, is_valid_status, is_absent_status, get_status_name, format_rate
from constants import STATUS_PRESENT, STATUS_EXCUSED_ABSENT, STATUS_UNEXCUSED_ABSENT

class ClassManager:
    def __init__(self, classes):
        self.classes = classes

    def class_exists(self, class_id):
        return self.find_class(class_id) is not None

    def find_class(self, class_id):
        return self.classes.find(lambda item: item.class_id == class_id)

    def add_class(self, class_id, class_name):
        if class_id == "" or class_name == "":
            print("Du lieu lop khong duoc de trong.")
            return False

        if self.class_exists(class_id):
            print("Ma lop da ton tai.")
            return False

        self.classes.append(ClassRoom(class_id, class_name))
        print("Da them lop hoc.")
        return True

    def input_add_class(self):
        print("\n=== Them lop hoc ===")
        class_id = input("Ma lop: ").strip()
        class_name = input("Ten lop/hoc phan: ").strip()
        return self.add_class(class_id, class_name)

    def display_all(self):
        print("\n=== Danh sach lop hoc ===")
        if self.classes.is_empty():
            print("Chua co lop hoc nao.")
            return

        current = self.classes.head
        index = 1
        while current is not None:
            classroom = current.data
            print(str(index) + ". " + classroom.class_id + " - " + classroom.class_name)
            index += 1
            current = current.next

    def input_find_class(self):
        print("\n=== Tim lop hoc ===")
        class_id = input("Nhap ma lop: ").strip()
        classroom = self.find_class(class_id)
        if classroom is None:
            print("Khong tim thay lop.")
        else:
            print("Ma lop: " + classroom.class_id)
            print("Ten lop: " + classroom.class_name)


class StudentManager:
    def __init__(self, students, class_manager):
        self.students = students
        self.class_manager = class_manager

    def student_exists_in_class(self, class_id, student_id):
        return self.find_student_in_class(class_id, student_id) is not None

    def find_student_in_class(self, class_id, student_id):
        return self.students.find(
            lambda item: item.class_id == class_id and item.student_id == student_id
        )

    def add_student(self, class_id, student_id, full_name):
        if class_id == "" or student_id == "" or full_name == "":
            print("Du lieu sinh vien khong duoc de trong.")
            return False

        if not self.class_manager.class_exists(class_id):
            print("Ma lop khong ton tai.")
            return False

        if self.student_exists_in_class(class_id, student_id):
            print("Sinh vien da ton tai trong lop nay.")
            return False

        self.students.append(Student(class_id, student_id, full_name))
        print("Da them sinh vien.")
        return True

    def input_add_student(self):
        print("\n=== Them sinh vien vao lop ===")
        class_id = input("Ma lop: ").strip()
        student_id = input("Ma sinh vien: ").strip()
        full_name = input("Ho ten: ").strip()
        return self.add_student(class_id, student_id, full_name)

    def display_students_by_class(self, class_id):
        print("\n=== Danh sach sinh vien lop " + class_id + " ===")
        if not self.class_manager.class_exists(class_id):
            print("Ma lop khong ton tai.")
            return

        current = self.students.head
        index = 1
        found = False
        while current is not None:
            student = current.data
            if student.class_id == class_id:
                print(str(index) + ". " + student.student_id + " - " + student.full_name)
                index += 1
                found = True
            current = current.next

        if not found:
            print("Lop nay chua co sinh vien.")

    def input_display_students_by_class(self):
        class_id = input("Nhap ma lop: ").strip()
        self.display_students_by_class(class_id)

    def input_find_student_by_id(self):
        print("\n=== Tim sinh vien theo ma ===")
        student_id = input("Ma sinh vien: ").strip()
        current = self.students.head
        found = False
        while current is not None:
            student = current.data
            if student.student_id == student_id:
                print("Lop: " + student.class_id + " | " + student.student_id + " - " + student.full_name)
                found = True
            current = current.next

        if not found:
            print("Khong tim thay sinh vien.")

    def count_students_by_class(self, class_id):
        return self.students.count_if(lambda item: item.class_id == class_id)


class ScheduleManager:
    def __init__(self, schedules, class_manager):
        self.schedules = schedules
        self.class_manager = class_manager

    def add_schedule(self, class_id, weekday, period, room):
        if class_id == "" or weekday == "" or period == "" or room == "":
            print("Du lieu thoi khoa bieu khong duoc de trong.")
            return False

        if not self.class_manager.class_exists(class_id):
            print("Ma lop khong ton tai.")
            return False

        self.schedules.append(Schedule(class_id, weekday, period, room))
        print("Da them lich hoc.")
        return True

    def input_add_schedule(self):
        print("\n=== Them thoi khoa bieu ===")
        class_id = input("Ma lop: ").strip()
        weekday = input("Thu: ").strip()
        period = input("Tiet: ").strip()
        room = input("Phong: ").strip()
        return self.add_schedule(class_id, weekday, period, room)

    def display_schedule_by_class(self, class_id):
        print("\n=== Thoi khoa bieu lop " + class_id + " ===")
        if not self.class_manager.class_exists(class_id):
            print("Ma lop khong ton tai.")
            return

        current = self.schedules.head
        index = 1
        found = False
        while current is not None:
            schedule = current.data
            if schedule.class_id == class_id:
                print(
                    str(index)
                    + ". "
                    + schedule.weekday
                    + " | "
                    + schedule.period
                    + " | Phong "
                    + schedule.room
                )
                index += 1
                found = True
            current = current.next

        if not found:
            print("Lop nay chua co thoi khoa bieu.")

    def input_display_schedule_by_class(self):
        class_id = input("Nhap ma lop: ").strip()
        self.display_schedule_by_class(class_id)


class AttendanceManager:
    def __init__(self, attendance_records, class_manager, student_manager):
        self.attendance_records = attendance_records
        self.class_manager = class_manager
        self.student_manager = student_manager

    def has_record(self, class_id, date, student_id):
        record = self.attendance_records.find(
            lambda item: item.class_id == class_id
            and item.date == date
            and item.student_id == student_id
        )
        return record is not None

    def add_record(self, class_id, date, student_id, status):
        if class_id == "" or date == "" or student_id == "" or status == "":
            print("Du lieu diem danh khong duoc de trong.")
            return False

        if not self.class_manager.class_exists(class_id):
            print("Ma lop khong ton tai.")
            return False

        if not self.student_manager.student_exists_in_class(class_id, student_id):
            print("Sinh vien khong ton tai trong lop nay.")
            return False

        if not is_valid_status(status):
            print("Trang thai khong hop le. Chi nhan CM, VCP, VKP.")
            return False

        if self.has_record(class_id, date, student_id):
            print("Sinh vien da duoc diem danh trong ngay nay.")
            return False

        self.attendance_records.append(AttendanceRecord(class_id, date, student_id, status))
        return True

    def input_attend_class_by_date(self):
        print("\n=== Diem danh lop theo ngay ===")
        class_id = input("Ma lop: ").strip()
        date = input("Ngay hoc (YYYY-MM-DD): ").strip()

        if not self.class_manager.class_exists(class_id):
            print("Ma lop khong ton tai.")
            return False

        current = self.student_manager.students.head
        found_student = False
        added_any = False

        while current is not None:
            student = current.data
            if student.class_id == class_id:
                found_student = True
                if self.has_record(class_id, date, student.student_id):
                    print(student.student_id + " - " + student.full_name + ": da co diem danh, bo qua.")
                else:
                    status = self.input_status_for_student(student)
                    if self.add_record(class_id, date, student.student_id, status):
                        added_any = True
            current = current.next

        if not found_student:
            print("Lop nay chua co sinh vien.")
            return False

        if added_any:
            print("Da ghi nhan diem danh.")
        else:
            print("Khong co ban ghi moi.")

        return added_any

    def input_status_for_student(self, student):
        while True:
            print("\n" + student.student_id + " - " + student.full_name)
            print("CM: Co mat | VCP: Vang co phep | VKP: Vang khong phep")
            status = input("Trang thai: ").strip().upper()
            if is_valid_status(status):
                return status
            print("Trang thai khong hop le.")

    def input_add_single_record(self):
        print("\n=== Them mot ban ghi diem danh ===")
        class_id = input("Ma lop: ").strip()
        date = input("Ngay hoc (YYYY-MM-DD): ").strip()
        student_id = input("Ma sinh vien: ").strip()
        status = input("Trang thai (CM/VCP/VKP): ").strip().upper()
        return self.add_record(class_id, date, student_id, status)

    def display_records_by_class_date(self, class_id, date):
        print("\n=== Diem danh lop " + class_id + " ngay " + date + " ===")
        current = self.attendance_records.head
        found = False
        index = 1

        while current is not None:
            record = current.data
            if record.class_id == class_id and record.date == date:
                student = self.student_manager.find_student_in_class(class_id, record.student_id)
                student_name = ""
                if student is not None:
                    student_name = student.full_name

                print(
                    str(index)
                    + ". "
                    + record.student_id
                    + " - "
                    + student_name
                    + " | "
                    + get_status_name(record.status)
                )
                found = True
                index += 1
            current = current.next

        if not found:
            print("Khong co du lieu diem danh.")

    def input_display_records_by_class_date(self):
        class_id = input("Ma lop: ").strip()
        date = input("Ngay hoc (YYYY-MM-DD): ").strip()
        self.display_records_by_class_date(class_id, date)

    def input_search_records_by_student_id(self):
        print("\n=== Tim diem danh theo ma sinh vien ===")
        student_id = input("Ma sinh vien: ").strip()
        current = self.attendance_records.head
        found = False
        while current is not None:
            record = current.data
            if record.student_id == student_id:
                student = self.student_manager.find_student_in_class(record.class_id, record.student_id)
                student_name = ""
                if student is not None:
                    student_name = student.full_name

                print(
                    "Lop "
                    + record.class_id
                    + " | "
                    + record.date
                    + " | "
                    + record.student_id
                    + " - "
                    + student_name
                    + " | "
                    + get_status_name(record.status)
                )
                found = True
            current = current.next

        if not found:
            print("Khong co lich su diem danh cua sinh vien nay.")

    def count_total_sessions(self, class_id, student_id):
        return self.attendance_records.count_if(
            lambda item: item.class_id == class_id and item.student_id == student_id
        )

    def count_absences(self, class_id, student_id):
        return self.attendance_records.count_if(
            lambda item: item.class_id == class_id
            and item.student_id == student_id
            and is_absent_status(item.status)
        )

    def calculate_absence_rate(self, class_id, student_id):
        total_sessions = self.count_total_sessions(class_id, student_id)
        if total_sessions == 0:
            return 0.0

        absence_count = self.count_absences(class_id, student_id)
        return absence_count * 100.0 / total_sessions


class ReportManager:
    def __init__(self, students, attendance_records, student_manager, attendance_manager, class_manager):
        self.students = students
        self.attendance_records = attendance_records
        self.student_manager = student_manager
        self.attendance_manager = attendance_manager
        self.class_manager = class_manager

    def input_session_statistics(self):
        print("\n=== Thong ke si so lop theo buoi ===")
        class_id = input("Ma lop: ").strip()
        date = input("Ngay hoc (YYYY-MM-DD): ").strip()
        self.display_session_statistics(class_id, date)

    def display_session_statistics(self, class_id, date):
        if not self.class_manager.class_exists(class_id):
            print("Ma lop khong ton tai.")
            return

        total_students = self.student_manager.count_students_by_class(class_id)
        present_count = 0
        excused_absent_count = 0
        unexcused_absent_count = 0

        current = self.attendance_records.head
        while current is not None:
            record = current.data
            if record.class_id == class_id and record.date == date:
                if record.status == STATUS_PRESENT:
                    present_count += 1
                elif record.status == STATUS_EXCUSED_ABSENT:
                    excused_absent_count += 1
                elif record.status == STATUS_UNEXCUSED_ABSENT:
                    unexcused_absent_count += 1
            current = current.next

        recorded_count = present_count + excused_absent_count + unexcused_absent_count
        missing_count = total_students - recorded_count
        if missing_count < 0:
            missing_count = 0

        print("\nLop: " + class_id)
        print("Ngay: " + date)
        print("Tong sinh vien: " + str(total_students))
        print("Da diem danh: " + str(recorded_count))
        print("Co mat: " + str(present_count))
        print("Vang co phep: " + str(excused_absent_count))
        print("Vang khong phep: " + str(unexcused_absent_count))
        print("Chua co ban ghi: " + str(missing_count))

    def input_most_absent_students(self):
        print("\n=== Danh sach sinh vien vang nhieu nhat ===")
        class_id = input("Nhap ma lop, bo trong de xem tat ca: ").strip()
        self.display_most_absent_students(class_id)

    def display_most_absent_students(self, class_id):
        if class_id != "" and not self.class_manager.class_exists(class_id):
            print("Ma lop khong ton tai.")
            return

        report_items = self.build_absence_report_items(class_id)
        if report_items.is_empty():
            print("Khong co sinh vien phu hop.")
            return

        self.sort_report_items_by_absence_desc(report_items)
        print("\nMa lop | Ma SV | Ho ten | So buoi vang | Tong buoi | Ty le vang")

        current = report_items.head
        index = 1
        while current is not None:
            item = current.data
            print(
                str(index)
                + ". "
                + item.student.class_id
                + " | "
                + item.student.student_id
                + " | "
                + item.student.full_name
                + " | "
                + str(item.absence_count)
                + " | "
                + str(item.total_sessions)
                + " | "
                + format_rate(item.absence_rate)
                + "%"
            )
            index += 1
            current = current.next

    def input_warning_students(self):
        print("\n=== Danh sach sinh vien nguy co cam thi ===")
        class_id = input("Nhap ma lop, bo trong de xem tat ca: ").strip()
        self.display_warning_students(class_id)

    def display_warning_students(self, class_id):
        if class_id != "" and not self.class_manager.class_exists(class_id):
            print("Ma lop khong ton tai.")
            return

        report_items = self.build_absence_report_items(class_id)
        self.sort_report_items_by_absence_desc(report_items)

        current = report_items.head
        found = False
        print("\nMa lop | Ma SV | Ho ten | So buoi vang | Tong buoi | Ty le vang")
        while current is not None:
            item = current.data
            if item.absence_rate > 20.0:
                print(
                    item.student.class_id
                    + " | "
                    + item.student.student_id
                    + " | "
                    + item.student.full_name
                    + " | "
                    + str(item.absence_count)
                    + " | "
                    + str(item.total_sessions)
                    + " | "
                    + format_rate(item.absence_rate)
                    + "% | Nguy co cam thi"
                )
                found = True
            current = current.next

        if not found:
            print("Khong co sinh vien vang qua 20%.")

    def build_absence_report_items(self, class_id):
        report_items = LinkedList()
        current = self.students.head
        while current is not None:
            student = current.data
            if class_id == "" or student.class_id == class_id:
                total_sessions = self.attendance_manager.count_total_sessions(
                    student.class_id, student.student_id
                )
                absence_count = self.attendance_manager.count_absences(
                    student.class_id, student.student_id
                )
                absence_rate = self.attendance_manager.calculate_absence_rate(
                    student.class_id, student.student_id
                )
                report_items.append(
                    AbsenceReportItem(student, total_sessions, absence_count, absence_rate)
                )
            current = current.next
        return report_items

    def sort_report_items_by_absence_desc(self, report_items):
        if report_items.head is None:
            return

        swapped = True
        while swapped:
            swapped = False
            current = report_items.head
            while current is not None and current.next is not None:
                first = current.data
                second = current.next.data
                should_swap = False

                if first.absence_count < second.absence_count:
                    should_swap = True
                elif first.absence_count == second.absence_count:
                    if first.absence_rate < second.absence_rate:
                        should_swap = True

                if should_swap:
                    temp = current.data
                    current.data = current.next.data
                    current.next.data = temp
                    swapped = True

                current = current.next
