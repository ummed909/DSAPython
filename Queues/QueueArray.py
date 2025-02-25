
class Queue:
    def __init__(self, size=30):
        self.size = size
        self.front=-1
        self.rear=-1
        self.queue = [None] * self.size

    def is_empty(self):
        if self.front==-1 or self.front > self.rear:
            return True
        else:
            return False

    def enqueue(self, value):
        self.rear += 1
        self.queue[self.rear]= value
        if self.front == -1:
            self.front = 0

    def dequeue(self):
        if self.front>self.rear:
            print("queue is empty")
            return
        item = self.queue[self.front]
        self.front +=1
        return item

    def get_front(self):
        return self.queue[self.front]

    def get_rear(self):
        return self.queue[self.rear]

    def get_size(self):
        if self.front == -1:
            return 0
        return self.rear-self.front+1