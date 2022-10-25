class MyCircularQueue:

    def __init__(self, k: int):
        self.max_length = k
        self.current_length = 0
        self.queue = [None] * k
        self.head = -1
        self.tail = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        tail = (self.tail + 1) % self.max_length
        self.queue[tail] = value
        self.tail = tail
        self.current_length += 1
        if self.current_length == 1:
            self.head = 0
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.head = (self.head + 1) % self.max_length
        self.current_length -= 1
        if self.isEmpty():
            self.head = -1
            self.tail = -1
        
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        return self.current_length == 0

    def isFull(self) -> bool:
        return self.current_length == self.max_length


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()