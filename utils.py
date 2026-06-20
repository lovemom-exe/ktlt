from constants import STATUS_PRESENT, STATUS_EXCUSED_ABSENT, STATUS_UNEXCUSED_ABSENT

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def is_empty(self):
        return self.head is None

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def find(self, condition):
        current = self.head
        while current is not None:
            if condition(current.data):
                return current.data
            current = current.next
        return None

    def count_if(self, condition):
        count = 0
        current = self.head
        while current is not None:
            if condition(current.data):
                count += 1
            current = current.next
        return count

    def remove(self, condition):
        previous = None
        current = self.head
        while current is not None:
            if condition(current.data):
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next

                if current == self.tail:
                    self.tail = previous

                self.size -= 1
                return True

            previous = current
            current = current.next

        return False

class TextParser:
    @staticmethod
    def get_field(text, index):
        current_index = 0
        result = ""
        i = 0
        while i < len(text):
            char = text[i]
            if char == "|":
                if current_index == index:
                    return result
                current_index += 1
                result = ""
            else:
                if current_index == index:
                    result += char
            i += 1

        if current_index == index:
            return result
        return ""

def is_valid_status(status):
    return (
        status == STATUS_PRESENT
        or status == STATUS_EXCUSED_ABSENT
        or status == STATUS_UNEXCUSED_ABSENT
    )

def is_absent_status(status):
    return status == STATUS_EXCUSED_ABSENT or status == STATUS_UNEXCUSED_ABSENT

def get_status_name(status):
    if status == STATUS_PRESENT:
        return "Co mat"
    if status == STATUS_EXCUSED_ABSENT:
        return "Vang co phep"
    if status == STATUS_UNEXCUSED_ABSENT:
        return "Vang khong phep"
    return "Khong xac dinh"

def format_rate(rate):
    return "{:.2f}".format(rate)
