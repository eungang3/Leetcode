class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index):
        if index < 0 or self.length <= index:
            return -1

        if self.head == None:
            return -1 

        current = self.head 
        for i in range(index):
            current = current.next 
        return current.value

    def addAtHead(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node 
        self.length += 1

    def addAtTail(self, val):
        current = self.head
        if not current:
            self.head = Node(val)
        else:
            while(current.next != None):
                current = current.next
            current.next = Node(val)
        self.length += 1
        
    def addAtIndex(self, index, val):
        if index < 0 or self.length < index:
            return 
        if index == 0:
            self.addAtHead(val)
        else:
            current = self.head 
            for i in range(index - 1):
                current = current.next
            new_node = Node(val)
            new_node.next = current.next
            current.next = new_node 

            self.length += 1
            
    def deleteAtIndex(self, index):
        if index < 0 or self.length <= index:
            return 
        
        current = self.head
        if index == 0:
            self.head = current.next
        else:   
            for i in range(index - 1):
                current = current.next 
            current.next = current.next.next

        self.length -= 1

    

    