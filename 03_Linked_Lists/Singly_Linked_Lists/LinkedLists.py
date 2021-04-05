from Node import Node


class LinkedLists:
    _head = None
    _size = 0

    # init lists
    def __init__(self):
        self._head = None
        self._size = 0

    # to string lists
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

    # count size lists
    def length(self):
        return self._size

    # check empty lists
    def isEmpty(self):
        return self._size == 0

    # O(n) push new data to linked lists
    def push(self, data):
        # create new node
        newNode = Node(data)
        # if empty => newNode = head
        if(self.isEmpty()):
            self._head = newNode
        else:
            current = self._head
            # while current to end (node null)
            while(current != None):
                if(current.getNext() == None):
                    current.setNext(newNode)
                    break
                current = current.getNext()

        # increase size
        self._size += 1
