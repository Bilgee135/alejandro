class Pair:
    def __init__(self, key, val):
        self.key = key
        self.val = val


class HashTable:
    
    def __init__(self, capacity: int):
        if capacity > 0:
            self.capacity = capacity
        self.size = 0 
        self.map = [None] * capacity

    def hash(self, key: int) -> int:
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        index = self.hash(key)

        while True:
            if self.map[index] == None:
                self.map[index] = Pair(key,value)
                self.size += 1
                if self.size / self.capacity >= 0.5:
                    self.resize()
                return
            elif self.map[index].key == key:
                self.map[index].val = value
                return

            index += 1
            index = index % self.capacity  


    def get(self, key: int) -> int:
        index = self.hash(key)

        while self.map[index] != None:
            if self.map[index].key == key:
                return self.map[index].val
            
            index += 1
            index = index % self.capacity 
        
        return -1

    def remove(self, key: int) -> bool:
        index = self.hash(key)
        
        while self.map[index] != None:
            if self.map[index].key == key:
                self.map[index] = None
                self.size -= 1
                # Rehash subsequent entries in the cluster to prevent breaking linear probing
                index = (index + 1) % self.capacity
                while self.map[index] is not None:
                    pair = self.map[index]
                    self.map[index] = None
                    self.size -= 1
                    self.insert(pair.key, pair.val)
                    index = (index + 1) % self.capacity
                return True

            index += 1 
            index = index % self.capacity 

        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity 

    def resize(self) -> None:
        self.capacity *= 2 
        newMap = [None] * self.capacity

        oldMap = self.map
        self.map = newMap
        self.size = 0
        for pair in oldMap:
            if pair:
                self.insert(pair.key, pair.val)
