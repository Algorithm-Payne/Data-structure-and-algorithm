from queue import LifoQueue


class Queue:

    def __init__(self):
        self.rear = None
        self.front = None
        self.r = 0
        self.f = 0

    def isEMpty(self):
        if self.r == self.f:
            print("The queue is empty")
        else:
            print("The queue is not empty")

    def push(self, data):
        if self.f == self.r:
            q = Queue(data)
            self.rear = q
            self.front = q
            self.r = 0
            self.f = 1
        else:
            q = Queue(data)
            self.rear.next = q
            self.rear = q
            self.f += 1

    def pop(self):
        if self.r == self.f:
            print("The Queue is empty")
            # return false
        else:
            self.front = self.front.next
            self.f = self.f - 1

    def top(self):
        if self.r == self.f:
            # print("empty")
            raise EOFError("empty")
        else:
            print(self.front.data)