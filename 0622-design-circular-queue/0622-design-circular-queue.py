class MyCircularQueue:
    def __init__(self, k: int):
        self.front = -1
        self.rear = -1
        self.max_size = k
        self.length = 0
        self.queue = [None] * k
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = value
        self.length += 1
        
        if self.length == 1:
            self.front = 0
        
        return True
        
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.front = (self.front + 1) % self.max_size
        self.length -= 1
        
        if self.isEmpty():
            self.front = -1
            self.rear = -1
        
        return True
        
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]
    
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.length == 0
        
    def isFull(self) -> bool:
        return self.length == self.max_size