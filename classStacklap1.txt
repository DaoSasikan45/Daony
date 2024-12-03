class Stack:
    def __init__(self, size):
        self.size = size
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) >= self.size

    def push(self, item):
        if not self.is_full():
            self.items.append(item)
            print(f"เพิ่มข้อมูล {item} ลงใน Stack สำเร็จ")
            return True
        else:
            print("Stack เต็มแล้ว ไม่สามารถเพิ่มข้อมูลได้")
            return False

    def pop(self):
        if not self.is_empty():
            item = self.items.pop()
            print(f"ลบข้อมูล {item} ออกจาก Stack สำเร็จ")
            return item
        else:
            print("Stack ว่างเปล่า ไม่สามารถลบข้อมูลได้")
            return None

    def display(self):
        if not self.is_empty():
            print("ข้อมูลใน Stack:", self.items)
        else:
            print("Stack ว่างเปล่า")

    def average(self):
        if not self.is_empty():
            avg = sum(self.items) / len(self.items)
            print(f"ค่าเฉลี่ยของข้อมูลใน Stack: {avg:.2f}")
        else:
            print("Stack ว่างเปล่า ไม่สามารถคำนวณค่าเฉลี่ยได้")



n = int(input("โปรดระบุขนาดของ Stack ที่มีขนาดตั้งแต่ 6 ช่องขึ้นไป = "))
while n < 6:
    n = int(input("โปรดระบุขนาดของ Stack ที่มีขนาดตั้งแต่ 6 ช่องขึ้นไป = "))


myStack = Stack(n)


while True:
    print("\nโปรดระบุทางเลือกในการดำเนินการกับ Stack")
    print("1. เพิ่มข้อมูลใน Stack")
    print("2. ลบข้อมูลจาก Stack")
    print("3. แสดงข้อมูลทั้งหมดที่จัดเก็บใน Stack")
    print("4. แสดงค่าเฉลี่ยของข้อมูลที่จัดเก็บใน Stack")
   

    try:
        p = int(input("ทางเลือกในการดำเนินการ = "))

        if p == 1:
            item = int(input("กรุณากรอกข้อมูลที่จะเพิ่มใน Stack: "))
            myStack.push(item)
        elif p == 2:
            myStack.pop()
        elif p == 3:
            myStack.display()
        elif p == 4:
            myStack.average()
        
            print("กรุณาเลือกเมนู 1-4 เท่านั้น")
    except ValueError:
        print("กรุณาป้อนตัวเลขจำนวนเต็ม")
