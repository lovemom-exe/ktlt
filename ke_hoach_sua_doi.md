# Kế hoạch sửa đổi project "Hệ thống quản lý điểm danh"

Dựa trên review repo `lovemom-exe/ktlt`, đối chiếu với `guide.txt`. Chia làm 4 giai đoạn, làm theo thứ tự để không bị rối.

---

## Giai đoạn 1 — Vệ sinh repo (~15 phút, làm trước tiên)

- [ ] Tạo file `.gitignore` ở thư mục gốc:
  ```
  __pycache__/
  *.pyc
  .idea/
  ```
- [ ] Gỡ các file đã lỡ commit ra khỏi git (vẫn giữ trên máy, chỉ bỏ khỏi tracking):
  ```bash
  git rm -r --cached __pycache__ .idea
  git commit -m "chore: cleanup pycache and IDE config"
  ```
- [ ] Xóa thư mục rỗng `prj/Attendace_Management_System` (tàn dư, không dùng tới):
  ```bash
  git rm -r prj
  git commit -m "chore: remove unused empty folder"
  ```

---

## Giai đoạn 2 — Bổ sung code còn thiếu (~1-2 giờ, ưu tiên cao)

### 2.1. Bắt buộc nên thêm: xem danh sách buổi học đã điểm danh của 1 lớp

Hiện tại không có object `Session` riêng nên không có cách liệt kê "lớp này đã điểm danh ngày nào". Thêm method vào `AttendanceManager` (giữ đúng style code hiện có — tự cài, không dùng `set()`):

```python
# managers.py — thêm vào class AttendanceManager
def get_sessions_by_class(self, class_id):
    """Tra ve LinkedList cac ngay da diem danh cua 1 lop, khong trung lap."""
    sessions = LinkedList()
    current = self.attendance_records.head
    while current is not None:
        record = current.data
        if record.class_id == class_id:
            already_added = sessions.find(lambda d: d == record.date)
            if already_added is None:
                sessions.append(record.date)
        current = current.next
    return sessions

def input_display_sessions_by_class(self):
    print("\n=== Danh sach buoi da diem danh ===")
    class_id = input("Ma lop: ").strip()
    if not self.class_manager.class_exists(class_id):
        print("Ma lop khong ton tai.")
        return
    sessions = self.get_sessions_by_class(class_id)
    if sessions.is_empty():
        print("Lop nay chua co buoi diem danh nao.")
        return
    current = sessions.head
    index = 1
    while current is not None:
        print(str(index) + ". " + current.data)
        index += 1
        current = current.next
```

Thêm vào `attendance_menu()` trong `app.py`:
```python
print("4. Xem danh sach buoi da diem danh")
...
elif choice == "4":
    self.attendance_manager.input_display_sessions_by_class()
```

- [ ] Thêm 2 hàm trên vào `managers.py`
- [ ] Thêm lựa chọn menu "4" vào `attendance_menu()` trong `app.py`
- [ ] Cập nhật `class_diagram.mmd` thêm 2 method này vào `AttendanceManager`
- [ ] Test thử: chạy chương trình, chọn lớp `IT001`, kỳ vọng thấy 3 ngày `2026-05-04`, `2026-05-07`, `2026-05-11`

### 2.2. Tùy chọn (nếu còn thời gian / muốn điểm thiết kế cao hơn): thêm Update/Delete

Hiện chỉ có Create + Read + Search. Nếu muốn bổ sung:
- [ ] `ClassManager.update_class(class_id, new_name)`, `delete_class(class_id)` — nhớ kiểm tra ràng buộc: không cho xóa lớp nếu còn sinh viên/điểm danh
- [ ] `StudentManager.delete_student(class_id, student_id)`
- [ ] `AttendanceManager`: cho sửa lại trạng thái điểm danh đã ghi nhận (hiện tại `add_record` từ chối nếu đã có bản ghi — có thể đổi thành "muốn sửa không?")

> Không bắt buộc theo đề, nhưng nếu bỏ qua thì nên ghi rõ trong báo cáo (mục 2 — mô tả thiết kế) là phạm vi có chủ đích giới hạn ở Create/Read/Search, để người chấm không nghĩ là thiếu sót.

---

## Giai đoạn 3 — Soạn báo cáo Word (~3-4 giờ, **bắt buộc**, ưu tiên cao nhất)

Nội dung kỹ thuật trong `BAO_CAO.md` đã khá đủ — phần lớn việc là **chuyển định dạng + bổ sung 2 phần đang thiếu**.

- [ ] **Thông tin người thực hiện**: họ tên, MSSV, lớp, GVHD. Nếu làm nhóm: bảng phân công ai làm phần nào.
- [ ] **Chụp ảnh kết quả chạy chương trình** cho từng test case trong bảng (mục 5 của `BAO_CAO.md` đã liệt kê 11 tình huống) — chạy chương trình thật, chụp màn hình terminal/console cho từng case, dán vào báo cáo ngay cạnh mô tả test case tương ứng.
- [ ] **Class diagram**: xuất `class_diagram.mmd` ra ảnh PNG (dùng [mermaid live editor](https://mermaid.live) dán code vào rồi export ảnh), chèn vào mục "Mô tả thiết kế".
- [ ] **Định dạng theo mẫu đồ án của trường**: font chữ, cỡ chữ, căn lề, header/footer, đánh số trang — lấy đúng file mẫu (.docx) của trường nếu có, hoặc theo chuẩn báo cáo thông thường (Times New Roman 13pt, giãn dòng 1.5, lề trên/dưới 2cm, trái 3cm, phải 2cm) nếu trường không cấp mẫu cụ thể.
- [ ] **Phụ lục code**: dán code hàm `main()` (đã có trong `BAO_CAO.md`) + mô tả ngắn các hàm xử lý chính (`add_record`, `calculate_absence_rate`, `sort_report_items_by_absence_desc`...)

Cấu trúc file Word đề xuất (theo đúng khung `guide.txt` yêu cầu):
```
1. Trang bìa (tên trường/môn, tên đề tài, người thực hiện, MSSV, GVHD)
2. Mô tả tổng thể chức năng
3. Thiết kế / tổ chức chương trình (sơ đồ lớp + giải thích) + file dữ liệu
4. Tình huống kiểm thử + kết quả (ảnh chụp)
5. Tổng kết kỹ thuật đã vận dụng
6. Phụ lục code
```

> Khi bạn đã có đủ: (1) tên/MSSV, (2) ảnh chụp kết quả test — báo lại mình, mình sẽ soạn trực tiếp file `.docx` hoàn chỉnh theo đúng nội dung kỹ thuật đã có sẵn trong `BAO_CAO.md`.

---

## Giai đoạn 4 — Đóng gói & nộp bài (~30 phút)

- [ ] Nén thư mục source (đã vệ sinh ở Giai đoạn 1) + thư mục `data/` thành `.zip` hoặc `.rar`
- [ ] Kiểm tra lại file nén **không chứa** `__pycache__/`, `.idea/`, file `.git/`
- [ ] In báo cáo Word để nộp & ký danh sách thi
- [ ] Tải 2 file (báo cáo Word + file nén code) lên assignment trên MS Teams

---

### Tóm tắt độ ưu tiên

| Việc | Bắt buộc? | Thời gian |
|---|---|---|
| Vệ sinh repo | Nên làm | 15 phút |
| Thêm "xem buổi đã điểm danh" | Nên làm | 30 phút |
| Update/Delete | Tùy chọn | 1-2 giờ |
| Báo cáo Word đầy đủ | **Bắt buộc** | 3-4 giờ |
| Đóng gói nộp bài | **Bắt buộc** | 30 phút |
