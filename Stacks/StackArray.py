class Stack:
    def __init__(self, size=30):
        self.stack = [None] * size
        self.top = -1

    def is_empty(self):
        return self.top==-1

    def search(self,x):
        for i in range(0, self.top):
            if self.stack[i] == x:
                return i
        return -1

    def push(self, value):
        self.top+=1
        self.stack[self.top]=value

    def pop(self):
        if self.top == -1:
            print("Stack is empty | underflow")
        else:
            node= self.stack[self.top]
            self.top -=1
            return node

    def get_size(self):
        n=0
        x=self.top
        while x!=-1:
            n+=1
            x -= 1
        return n

    def get_top(self):
        return self.stack[self.top]