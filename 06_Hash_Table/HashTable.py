class HashTable:

    def __init__(self):
        self.max = 10
        self.arr = [[] for i in range(self.max)]

    def hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max

    def add(self, key, value):
        h = self.hash(key)
        found = False

        # check key exists
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
        if not found:
            self.arr[h].append((key, value))

    def get(self, key):
        h = self.hash(key)
        for kv in self.arr[h]:
            if kv[0] == key:
                return kv[1]

    def remove(self, key):
        h = self.hash(key)
        temp = None
        for index, kv in enumerate(self.arr[h]):
            if kv[0] == key:
                temp = self.arr[h][index]
                del self.arr[h][index]
        return temp

    def exists(self, key):
        h = self.hash(key)
        for kv in self.arr[h]:
            if kv[0] == key:
                return True
        return False
