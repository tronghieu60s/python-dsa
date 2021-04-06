class Node:

    def __init__(self, data):
        self._data = data
        self._next = None

    def getData(self):
        return self._data

    def setData(self, data):
        self._data = data

    def getNext(self):
        return self._next

    def setNext(self, next):
        self._next = next