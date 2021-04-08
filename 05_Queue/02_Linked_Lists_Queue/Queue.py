from Node import Node

class Queue:

    def __init__(self):
        self.head = self.tail = None

    def empty(self):
        return self.head == None

    def enqueue(self, value):
        temp = Node(value)

        if(self.tail == None):
            self.head = self.tail = temp
            return

        self.tail.next = temp
        self.tail = temp

    def dequeue(self):
        if self.empty():
            raise Exception("Queue Empty!")

        temp = self.head
        self.head = temp.next

        if(self.head == None):
            self.tail = None

        return temp.data