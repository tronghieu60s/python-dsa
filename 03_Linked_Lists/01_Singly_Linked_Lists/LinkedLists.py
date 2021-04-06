from Node import Node


class LinkedLists:

    # init lists
    def __init__(self):
        self._head = None
        self._size = 0

    # O(1)
    def length(self):
        return self._size

    # O(1)
    def isEmpty(self):
        return self._size == 0

    # O(n)
    def indexOf(self, data):
        index = 0
        current = self._head

        while(current != None):
            if(current.getData() == data):
                return index
            index += 1
            current = current.getNext()

        return -1

    # O(n)
    def clear(self):
        current = self._head
        while(current != None):
            # set head = next and set none current
            self._head = current.getNext()
            current = None
            current = self._head
        self._size = 0

    # O(n)
    def toString(self):
        result = ""
        current = self._head
        # while current to end (node null)
        while(current != None):
            result += current.getData()
            # if have next node => add more icon
            if(current.getNext() != None):
                result += " --> "
            else:
                result += " --> null"
            # set current
            current = current.getNext()
        return result

    # O(n)
    def addLast(self, data):
        # create new node
        newNode = Node(data)

        # if empty => newNode = head
        if(self.isEmpty()):
            self._head = newNode
        else:
            current = self._head
            # loop to last node
            while(current.getNext() != None):
                current = current.getNext()
            # set new node
            current.setNext(newNode)

        # increase size
        self._size += 1

    # O(1)
    def addFirst(self, data):
        # create new node
        newNode = Node(data)

        # set next new node to head and set head = new node
        newNode.setNext(self._head)
        self._head = newNode

        # increase size
        self._size += 1

    # O(n)
    def add(self, index, data):
        if(index == 0):
            self.addFirst(data)
            return

        currentIndex = 0
        current = self._head
        newNode = Node(data)

        while(current != None):
            if(currentIndex == index - 1):
                newNode.setNext(current.getNext())
                current.setNext(newNode)
                self._size += 1
                break

            currentIndex += 1
            current = current.getNext()

    # O(1)
    def removeFirst(self):
        if(self.isEmpty()):
            raise Exception("Lists Empty. Can Not Remove!")

        # set head = head next
        self._head = self._head.getNext()
        self._size -= 1

    # O(n)
    def removeLast(self):
        if(self.isEmpty()):
            raise Exception("Lists Empty. Can Not Remove!")

        # get second last and remove
        secondLast = self._head
        while(secondLast.getNext().getNext() != None):
            secondLast = secondLast.getNext()
        secondLast.setNext(None)

        # decrease size
        self._size -= 1

    # O(n)
    def remove(self, data):
        current = self._head
        preNode = None

        while(current != None):
            if(current.getData() == data):
                preNode.setNext(current.getNext())
                current.setNext(None)
                self._size -= 1

            preNode = current
            current = current.getNext()