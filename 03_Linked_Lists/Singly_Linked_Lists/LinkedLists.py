from Node import Node

class ListsEmptyException(Exception):
    pass

class LinkedLists:
    _head = None
    _size = 0

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

    # O()
    def clear(self):
        pass

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

    # O()
    def add(self, index, data):
        pass

    # O(1)
    def removeFirst(self):
        if(self.isEmpty()):
            raise Exception

        self._head = self._head.getNext()
        self._size -= 1

    # O(n)
    def removeLast(self):
        pass

    # O()
    def remove(self, data):
        pass

    # O()
    def removeAt(self, index):
        pass
