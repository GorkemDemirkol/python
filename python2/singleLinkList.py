class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SingleLinkList:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        last_node=self.head
        while last_node.next:
            last_node=last_node.next
        last_node.next=new_node
    def display(self):
        current_node=self.head
        while current_node:
            print(current_node.data,end=" => ")
            current_node=current_node.next
        print("None")

slink=SingleLinkList()
slink.append(1)
slink.append(2)
slink.append(3)
slink.append(4)
print("tek bağlantılı liste:")
slink.display()

class DoubleNode:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DoubleLinkList:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=DoubleNode(data)
        if not self.head:
            self.head=new_node
            return
        last_node=self.head
        while last_node.next:
            last_node=last_node.next
        last_node.next=new_node
        new_node.prev=last_node
    def display(self):
        current_node=self.head
        while current_node:
            print(current_node.data,end=" => ")
            current_node=current_node.next
        print("None")
    def display_reverse(self):
        current_node=self.head
        while current_node.next:
            current_node=current_node.next
        while current_node:
            print(current_node.data,end=" <=> ")
            current_node=current_node.prev
        print("None")
print("çift bağlantılı liste:")
dll=DoubleLinkList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.display()
dll.display_reverse()
#siderın verdiği örnek
class DoubleNode:  
    def __init__(self, data):  
        self.data = data  
        self.next = None  
        self.prev = None  

class DoubleLinkList:  
    def __init__(self):  
        self.head = None  
        self.tail = None  

    def append(self, data):  
        new_node = DoubleNode(data)  
        if not self.head:  
            self.head = new_node  
            self.tail = new_node  
            return  
        self.tail.next = new_node  
        new_node.prev = self.tail  
        self.tail = new_node  

    def prepend(self, data):  
        new_node = DoubleNode(data)  
        if not self.head:  
            self.head = new_node  
            self.tail = new_node  
            return  
        new_node.next = self.head  
        self.head.prev = new_node  
        self.head = new_node  

    def delete(self, key):  
        current_node = self.head  
        while current_node:  
            if current_node.data == key:  
                if current_node.prev:  
                    current_node.prev.next = current_node.next  
                if current_node.next:  
                    current_node.next.prev = current_node.prev  
                if current_node == self.head:  # Eğer baş düğüm siliniyorsa  
                    self.head = current_node.next  
                if current_node == self.tail:  # Eğer son düğüm siliniyorsa  
                    self.tail = current_node.prev  
                return  
            current_node = current_node.next  

    def display(self):  
        current_node = self.head  
        while current_node:  
            print(current_node.data, end=" <-> ")  
            current_node = current_node.next  
        print("None")  

    def display_reverse(self):  
        current_node = self.tail  
        while current_node:  
            print(current_node.data, end=" <-> ")  
            current_node = current_node.prev  
        print("None")  

    def search(self, key):  
        current_node = self.head  
        while current_node:  
            if current_node.data == key:  
                return current_node  
            current_node = current_node.next  
        return None  

    def length(self):  
        count = 0  
        current_node = self.head  
        while current_node:  
            count += 1  
            current_node = current_node.next  
        return count  

#Kullanım örneği  
print("çift bağlantılı liste:")
dll = DoubleLinkList()  
dll.append(1)  
dll.append(2)  
dll.append(3)  
dll.prepend(0)  
dll.append(4)

dll.display()  # 0 <-> 1 <-> 2 <-> 3 <-> None  
dll.display_reverse()  # 3 <-> 2 <-> 1 <-> 0 <-> None  
dll.delete(2)  
dll.display()  # 0 <-> 1 <-> 3 <-> None  

print("Length of the list:", dll.length())  # Length of the list: 3  
print("Searching for 1:", dll.search(1) is not None)  # Searching for 1: True  