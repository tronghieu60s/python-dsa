class Queue:

    def __init__(self, maxSize):
        self.head = self.tail = -1
        self.arr = [None] * maxSize

    def full(self):
        return self.tail == len(self.arr) - 1

    def empty(self):
        return self.head == -1

    def enqueue(self, value):

        if(self.full()):
            raise Exception("Full Queue!")

        if(self.empty()):
            self.head += 1

        self.tail += 1
        self.arr[self.tail] = value

    def dequeue(self):

        if(self.empty()):
            raise Exception("Empty Queue!")

        temp = self.arr[self.head]
        self.arr[self.head] = None
        if(self.head == self.tail):
            self.head = self.tail = -1
        else:
            self.head += 1

        return temp
