class MyCircularQueue:
    def __init__(self, k: int):
        self.max_length = k
        self.current_length = 0
        self.queue = [None] * k 
        self.front_index = -1 
        self.rear_index = -1 

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.rear_index = (self.rear_index + 1) % self.max_length
        self.queue[self.rear_index] = value
        self.current_length += 1
        if self.current_length == 1:
            self.front_index = 0

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.front_index = (self.front_index + 1) % self.max_length
        self.current_length -= 1
        if self.isEmpty():
            self.front_index = -1
            self.rear_index = -1
        
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front_index]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear_index]

    def isEmpty(self) -> bool:
        return self.current_length == 0

    def isFull(self) -> bool:
        return self.current_length == self.max_length
