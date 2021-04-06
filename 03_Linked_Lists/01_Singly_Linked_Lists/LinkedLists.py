from Node import Node


class LinkedLists:

    # init lists
    def __init__(self):
        self._head = None
        self._size = 0

    # O(n)
    def to_string(self):
        result = ""
        current = self._head
        # while current to end (node null)
        while(current):
            result += current.getData()
            # if have next node => add more icon
            if(current.getNext() != None):
                result += " --> "
            else:
                result += " --> null"
            # set current
            current = current.getNext()
        return result

    # O(1)
    def size(self):
        return self._size

    # O(1)
    def empty(self):
        return self._size == 0

    # O(n)
    def value_at(self, index):
        currentindex = 0
        current = self._head

        while(current):
            if(currentindex == index):
                return current.getData()
            currentindex += 1
            current = current.getNext()
        
        return None

    # O(1)
    def push_front(self, data):
        # create new node
        newNode = Node(data)

        # set next new node to head and set head = new node
        newNode.setNext(self._head)
        self._head = newNode

        # increase size
        self._size += 1

    # O(1)
    def pop_front(self):
        if(self.empty()):
            raise OverflowError("Lists Empty. Can Not Remove!")

        headData = self._head.getData()
        # set head = head next
        self._head = self._head.getNext()
        self._size -= 1

        return headData

    # O(n)
    def push_back(self, data):
        # create new node
        newNode = Node(data)

        # if empty => newNode = head
        if(self.empty()):
            self._head = newNode
        else:
            current = self._head
            # loop to last node
            while(current.getNext()):
                current = current.getNext()
            # set new node
            current.setNext(newNode)

        # increase size
        self._size += 1

    # O(n)
    def pop_back(self):
        if(self.empty()):
            raise OverflowError("Lists Empty. Can Not Remove!")

        # get second last and remove
        secondLast = self._head
        while(secondLast.getNext().getNext()):
            secondLast = secondLast.getNext()

        lastData = secondLast.getNext().getData()
        secondLast.setNext(None)

        # decrease size
        self._size -= 1

        return lastData

    # O(1)
    def front(self):
        if(self.empty()):
            raise OverflowError("Lists Empty. Can Not Access!")

        return self._head.getData()

    # O(n)
    def back(self):
        if(self.empty()):
            raise OverflowError("Lists Empty. Can Not Access!")

        return self.value_at(self._size - 1)
    
    # O(n)
    def insert(self, index, value):
        if(index == 0):
            self.addFirst(value)
            return

        currentIndex = 0
        current = self._head
        newNode = Node(value)

        while(current):
            if(currentIndex == index - 1):
                newNode.setNext(current.getNext())
                current.setNext(newNode)
                self._size += 1
                break

            currentIndex += 1
            current = current.getNext()

    # O(n)
    def erase(self, index):
        if(index == 0):
            self.pop_front()
            return

        currentIndex = 0
        current = self._head
        preNode = None

        while(current):
            if(currentIndex == index):
                preNode.setNext(current.getNext())
                current.setNext(None)
                break

            currentIndex += 1
            preNode = current
            current = current.getNext()

    # O(n)
    def value_n_from_end(self, n):
        return self.value_at(self._size - n)

    # O()
    def reverse(self):
        # define 3 variable
        prev = None
        current = self._head
        next = None

        # move pointer
        while(current):
            next = current.getNext()
            current.setNext(prev)
            prev = current
            current = next
        
        self._head = prev

    # O(n)
    def remove_value(self, value):
        current = self._head
        preNode = None

        while(current):
            if(current.getData() == value):
                if(current == self._head):
                    self.pop_front()
                    break

                preNode.setNext(current.getNext())
                current.setNext(None)
                self._size -= 1
                break

            preNode = current
            current = current.getNext()
        
