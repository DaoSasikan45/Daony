class Node:
    def __init__(self, info):
        self.info = info
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.n = 0  

    def add_front(self, info):  
        new_node = Node(info)
        if not self.head:  
            self.head = new_node
            self.tail = new_node
        else:  
            new_node.next = self.head
            self.head = new_node
        self.n += 1  

    def add_back(self, info):  
        new_node = Node(info)
        if not self.head:  
            self.head = new_node
            self.tail = new_node
        else:  
            self.tail.next = new_node
            self.tail = new_node
        self.n += 1  

    def display(self):
        current = self.head
        print("\nข้อมูลใน Singly Linked List:")
        while current:
            print(current.info, end=" -> ")
            current = current.next
        print("None")  
        print(f"ข้อมูลที่เก็บในตำแหน่งที่พอยน์เตอร์ head คือ: {self.head.info if self.head else None}")
        print(f"ข้อมูลที่เก็บในตำแหน่งที่พอยน์เตอร์ tail คือ: {self.tail.info if self.tail else None}")
        print(f"จำนวนข้อมูลใน Singly Linked List คือ: {self.n}")


linked_list = SLinkedList()

    print("การเลือกในการดำเนินการกับ Singly Linked List")
    print("B : เพิ่มข้อมูลที่จุดเริ่มต้นของ Singly Linked List")
    print("E : เพิ่มข้อมูลแบบต่อจากโหนดสุดท้ายของ Singly Linked List")
     choice = input("การเลือกในการดำเนินการ = ").strip().upper()
    
 while DD in ('B', 'E'):
    data = int(input ("ป้อนข้อมูล: "))
        if DD == 'B':
            list.AtTheBegining()
        else:
            list.AtTheEnd (info)
            list.display ( )
info = input ("กรุณาเลือก B หรือ E:")
print ("<ภผลลัพธ์สุดท้าย : ")
list.display ( )
if list.head:
print (E"ข้อมูลที่ตำแหน่งที่พอยน์เดอร์ head: (list.head.info)")
print (E"ข้อมูลที่ตำแหน่งที่พอยน์เตอร์ tail: (list.tail.info)")
print (f"ค่าเฉลี่ยของข้อมูล: (1ist.calculate_average (): : 2f)")
else:
print ("ไม่มีข้อมูลใน Linked List")
