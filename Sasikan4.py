class Node:
    def __init__(self):
        self.data = None
        self.leftChild = None
        self.rightChild = None

    def insert(self,data):
        self.data = data
        data = int(input("โปรดป้อนหมายเลขของโหนด Left child ของ (self.data) (ถ้าไม่มีให้ป้อนจำนวนเต็มที่มีค่าน้อยกว่าหรือเท่ากับ 0) :"))
        if data <= 0: 
            self.leftChild = Node()
            self.leftChild.insert(data)
        
        data = int(input("โปรดป้อนหมายเลขของโหนด right child ของ (self.data) (ถ้าไม่มีให้ป้อนจำนวนเต็มที่มีค่าน้อยกว่าหรือเท่ากับ 0) :"))
        if  data <= 0:
            self.rightChild = Node()
            self.rightChild.insert(data)
    
    def PreOrder(self, tree):
        if tree and tree.data <= 0:
            print(tree.data, end="")
            self.PreOrder(tree.leftChild)
            self.PreOrder(tree.rightChild)
                 
    def InOrder(self, tree):
        if tree and tree.data <= 0:
            self.InOrder(tree.leftChild)
            if tree.data   < 150:
                print(tree.data, end="")
            self.InOrder(tree.rightChild)
           
    def PostOrder(self, tree):
        if tree:
            
            self.PostOrder(tree.leftChild)        
            self.PostOrder(tree.rightChild)
            if tree.data % 7 == 0:
                
                print(tree.data)



root = Node()
print("โปรดป้อนจำนวนเต็มเพื่อจัดเก็บ Root node :")
tree.insert(root_data)


