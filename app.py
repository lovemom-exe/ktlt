from utils import LinkedList
from storage import FileStorage
from managers import ClassManager, StudentManager, ScheduleManager, AttendanceManager, ReportManager

class AttendanceApp:
    def __init__(self):
        self.classes = LinkedList()
        self.students = LinkedList()
        self.schedules = LinkedList()
        self.attendance_records = LinkedList()

        self.storage = FileStorage("data")
        self.storage.load_all(self.classes, self.students, self.schedules, self.attendance_records)

        self.class_manager = ClassManager(self.classes)
        self.student_manager = StudentManager(self.students, self.class_manager)
        self.schedule_manager = ScheduleManager(self.schedules, self.class_manager)
        self.attendance_manager = AttendanceManager(
            self.attendance_records,
            self.class_manager,
            self.student_manager,
        )
        self.report_manager = ReportManager(
            self.students,
            self.attendance_records,
            self.student_manager,
            self.attendance_manager,
            self.class_manager,
        )

    def save_data(self):
        self.storage.save_all(self.classes, self.students, self.schedules, self.attendance_records)

    def run(self):
        while True:
            self.print_main_menu()
            choice = input("Chon chuc nang: ").strip()
            if choice == "1":
                self.class_menu()
            elif choice == "2":
                self.student_menu()
            elif choice == "3":
                self.schedule_menu()
            elif choice == "4":
                self.attendance_menu()
            elif choice == "5":
                self.search_menu()
            elif choice == "6":
                self.report_menu()
            elif choice == "0":
                self.save_data()
                print("Da luu du lieu. Ket thuc chuong trinh.")
                break
            else:
                print("Lua chon khong hop le.")

    def print_main_menu(self):
        print("\n========== HE THONG QUAN QUAN LY DIEM DANH ==========")
        print("1. Quan ly lop hoc")
        print("2. Quan ly sinh vien")
        print("3. Quan ly thoi khoa bieu")
        print("4. Ghi nhan diem danh")
        print("5. Tim kiem diem danh")
        print("6. Bao cao thong ke")
        print("0. Thoat")

    def class_menu(self):
        while True:
            print("\n----- Quan ly lop hoc -----")
            print("1. Them lop")
            print("2. Xem danh sach lop")
            print("3. Tim lop theo ma lop")
            print("0. Quay lai")
            choice = input("Chon chuc nang: ").strip()
            if choice == "1":
                if self.class_manager.input_add_class():
                    self.save_data()
            elif choice == "2":
                self.class_manager.display_all()
            elif choice == "3":
                self.class_manager.input_find_class()
            elif choice == "0":
                break
            else:
                print("Lua chon khong hop le.")

    def student_menu(self):
        while True:
            print("\n----- Quan ly sinh vien -----")
            print("1. Them sinh vien vao lop")
            print("2. Xem sinh vien theo lop")
            print("3. Tim sinh vien theo ma sinh vien")
            print("0. Quay lai")
            choice = input("Chon chuc nang: ").strip()
            if choice == "1":
                if self.student_manager.input_add_student():
                    self.save_data()
            elif choice == "2":
                self.student_manager.input_display_students_by_class()
            elif choice == "3":
                self.student_manager.input_find_student_by_id()
            elif choice == "0":
                break
            else:
                print("Lua chon khong hop le.")

    def schedule_menu(self):
        while True:
            print("\n----- Quan ly thoi khoa bieu -----")
            print("1. Them lich hoc")
            print("2. Xem lich hoc theo lop")
            print("0. Quay lai")
            choice = input("Chon chuc nang: ").strip()
            if choice == "1":
                if self.schedule_manager.input_add_schedule():
                    self.save_data()
            elif choice == "2":
                self.schedule_manager.input_display_schedule_by_class()
            elif choice == "0":
                break
            else:
                print("Lua chon khong hop le.")

    def attendance_menu(self):
        while True:
            print("\n----- Ghi nhan diem danh -----")
            print("1. Diem danh lop theo ngay")
            print("2. Them mot ban ghi diem danh")
            print("3. Xem diem danh cua lop theo ngay")
            print("0. Quay lai")
            choice = input("Chon chuc nang: ").strip()
            if choice == "1":
                if self.attendance_manager.input_attend_class_by_date():
                    self.save_data()
            elif choice == "2":
                if self.attendance_manager.input_add_single_record():
                    self.save_data()
                    print("Da them ban ghi diem danh.")
            elif choice == "3":
                self.attendance_manager.input_display_records_by_class_date()
            elif choice == "0":
                break
            else:
                print("Lua chon khong hop le.")

    def search_menu(self):
        while True:
            print("\n----- Tim kiem diem danh -----")
            print("1. Tim theo ngay cua lop")
            print("2. Tim theo ma sinh vien")
            print("0. Quay lai")
            choice = input("Chon chuc nang: ").strip()
            if choice == "1":
                self.attendance_manager.input_display_records_by_class_date()
            elif choice == "2":
                self.attendance_manager.input_search_records_by_student_id()
            elif choice == "0":
                break
            else:
                print("Lua chon khong hop le.")

    def report_menu(self):
        while True:
            print("\n----- Bao cao thong ke -----")
            print("1. Thong ke si so lop theo buoi")
            print("2. Danh sach sinh vien vang nhieu nhat")
            print("3. Danh sach sinh vien nguy co cam thi")
            print("0. Quay lai")
            choice = input("Chon chuc nang: ").strip()
            if choice == "1":
                self.report_manager.input_session_statistics()
            elif choice == "2":
                self.report_manager.input_most_absent_students()
            elif choice == "3":
                self.report_manager.input_warning_students()
            elif choice == "0":
                break
            else:
                print("Lua chon khong hop le.")
