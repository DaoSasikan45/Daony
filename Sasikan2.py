class CircularQueue:
    def __init__(self, n):
        self.n = n
        self.queue = [None] * n
        self.front = -1
        self.rear = -1


    
    def enqueue(self, data):
         if ((self.rear + 1) % self.quantity == self.front):
            print("เพิ่มข้อมูลไม่ได้เพราะคิววงกลมเต็ม")
            return False  
        elif (self.front == -1): n 
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data  
            print("เพิ่มข้อมูลเข้าคิวสำเร็จ")
        else:
            self.rear = (self.rear + 1) % self.n
            self.queue[self.rear] = data 
            print("เพิ่มข้อมูลเข้าคิวสำเร็จ")
        return True

    def enqueue(self, data):
        if ((self.rear + 1) % self.n == self.front):
            print("เพิ่มข้อมูลไม่ได้เพราะคิววงกลมเต็ม")
            return False  
        elif (self.front == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data  
            print("เพิ่มข้อมูลเข้าคิวสำเร็จ")
        else:
            self.rear = (self.rear + 1) % self.n
            self.queue[self.rear] = data 
            print("เพิ่มข้อมูลเข้าคิวสำเร็จ")
        return True

    def dequeue(self):
        if (self.front == -1):
            print("ลบข้อมูลไม่ได้เพราะคิววงกลมว่าง")
            return None
        elif (self.front == self.rear):
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            print("ลบข้อมูลออกจากคิวสำเร็จ")
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.n
            print("ลบข้อมูลออกจากคิวสำเร็จ")

    def display_less_than_150(self):
        if (self.front == -1):
            print("แสดงข้อมูลไม่ได้เพราะคิววงกลมว่าง")
            return

        found = False
        print("ข้อมูลที่น้อยกว่า 150 ในคิว:")
        
        if self.rear >= self.front:
            for i in range(self.front, self.rear + 1):
                if self.queue[i] is not None and self.queue[i] < 150:
                    print(self.queue[i], end=" ")
                    found = True
        else:
            for i in range(self.front, self.quantity):
                if self.queue[i] is not None and self.queue[i] < 150:
                    print(self.queue[i], end=" ")
                    found = True
            for i in range(0, self.rear + 1):
                if self.queue[i] is not None and self.queue[i] < 150:
                    print(self.queue[i], end=" ")
                    found = True
        if not found:
            print("ไม่มีข้อมูลที่น้อยกว่า 150")
        print()

while True:
    n = int(input("โปรดระบุขนาดของคิววงกลมที่มีขนาดตั้งแต่ 5 ช่อง: "))
    if n >= 5:
        break
    print("ขนาดของคิววงกลมต้องมีขนาดตั้งแต่ 5 ช่อง: ")

q = CircularQueue(n)

while True:
    print("\nโปรดระบุทางเลือกในการดำเนินการ") 
    print("1. เพิ่มข้อมูลตัวเลขจำนวนเต็มในคิววงกลม")
    print("2. ลบข้อมูลที่จัดเก็บในคิววงกลม 1 ตัว")
    print("3. แสดงตัวเลขจำนวนเต็มที่มีค่าน้อยกว่า 150 ที่จัดเก็บในคิววงกลมทางจอภาพ")
    
    choice = int(input("ทางเลือกในการดำเนินการ = "))
    
    if choice == 1:
        data = int(input("ตัวเลขจำนวนเต็ม: "))
        q.enqueue(data)
    elif choice == 2:
        q.dequeue()
    elif choice == 3:
        q.display_less_than_150()
    else:
        break
