# Bao cao bai tap lon: He thong quan ly diem danh

## 1. Mo ta de tai

Chuong trinh quan ly diem danh lop hoc theo ngay. Moi sinh vien co ma sinh vien, ho ten va thuoc mot lop hoc cu the. He thong cho phep quan ly lop, sinh vien, thoi khoa bieu, ghi nhan diem danh va tao bao cao thong ke.

Trang thai diem danh gom:

- `CM`: Co mat
- `VCP`: Vang co phep
- `VKP`: Vang khong phep

Sinh vien co ty le vang tren 20% se duoc canh bao nguy co cam thi.

## 2. Thiet ke chuong trinh

Chuong trinh duoc thiet ke theo huong doi tuong, moi nhom chuc nang nam trong mot class rieng:

- `Node`, `LinkedList`: cau truc danh sach lien ket don tu cai dat.
- `ClassRoom`, `Student`, `Schedule`, `AttendanceRecord`: cac thuc the du lieu.
- `ClassManager`: quan ly lop hoc.
- `StudentManager`: quan ly sinh vien.
- `ScheduleManager`: quan ly thoi khoa bieu.
- `AttendanceManager`: ghi nhan va tim kiem diem danh.
- `ReportManager`: thong ke si so, sap xep sinh vien vang nhieu, canh bao vang tren 20%.
- `FileStorage`: doc/ghi file text.
- `AttendanceApp`: menu chinh va dieu phoi cac manager.

## 3. File du lieu

Du lieu nam trong thu muc `data`:

```text
data/classes.txt
data/students.txt
data/schedules.txt
data/attendance.txt
```

Dinh dang file:

```text
classes.txt: CLASS_ID|CLASS_NAME
students.txt: CLASS_ID|STUDENT_ID|FULL_NAME
schedules.txt: CLASS_ID|WEEKDAY|PERIOD|ROOM
attendance.txt: CLASS_ID|DATE|STUDENT_ID|STATUS
```

## 4. Ky thuat va thuat toan da van dung

- Lap trinh huong doi tuong.
- Danh sach lien ket don tu cai dat thay cho `list`.
- Tim kiem tuyen tinh tren danh sach lien ket.
- Doc file tung dong, khong dung `readlines()`.
- Tach truong du lieu bang ham tu cai dat, khong dung `split()`.
- Sap xep noi bot tren danh sach lien ket bang cach hoan doi du lieu node.
- Tinh ty le vang:

```text
ty le vang = so buoi vang / tong so buoi diem danh * 100
```

## 5. Kiem thu

Mot so test case chinh:

| STT | Tinh huong | Ket qua mong doi |
| --- | --- | --- |
| 1 | Them lop voi ma lop moi | Lop duoc them va luu file |
| 2 | Them lop trung ma | Chuong trinh bao trung ma |
| 3 | Them sinh vien vao lop co san | Sinh vien duoc them |
| 4 | Them sinh vien vao lop khong ton tai | Chuong trinh bao loi |
| 5 | Diem danh sinh vien theo ngay | Ban ghi duoc luu vao `attendance.txt` |
| 6 | Diem danh trung cung lop, ngay, sinh vien | Chuong trinh tu choi |
| 7 | Tim diem danh theo ngay cua lop | Hien dung cac ban ghi cua ngay do |
| 8 | Tim theo ma sinh vien | Hien lich su diem danh cua sinh vien |
| 9 | Bao cao si so theo buoi | Dem dung co mat, vang co phep, vang khong phep |
| 10 | Bao cao vang nhieu nhat | Sap xep giam dan theo so buoi vang |
| 11 | Canh bao vang tren 20% | Hien sinh vien nguy co cam thi |

## 6. Huong dan chay

Chay lenh:

```powershell
python main.py
```

Sau do chon chuc nang trong menu console.

## 7. Phu luc code chinh

Ham `main` trong `main.py`:

```python
def main():
    app = AttendanceApp()
    app.run()
```

`AttendanceApp` tao cac danh sach lien ket, nap du lieu tu file, khoi tao cac manager va hien thi menu cho nguoi dung thao tac den khi chon thoat.
