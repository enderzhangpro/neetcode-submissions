class HashTable:

    def _hash(self, key):
        return hash(key) % self.capacity
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.length = 0

    def insert(self, key: int, value: int) -> None:      
        hashed_key = self._hash(key)
        while self.array[hashed_key] is not None:
            if self.array[hashed_key][0] == key:
                self.array[hashed_key][1] = value
                return
            hashed_key = (hashed_key + 1) % self.capacity
        
        self.array[hashed_key] = [key, value]
        self.length += 1
        if self.length >= self.capacity / 2:
            self.resize()

    def get(self, key: int) -> int:
        hashed_key = self._hash(key)
        start_index = hashed_key
        while self.array[hashed_key] is not None:
            if self.array[hashed_key][0] == key:
                return self.array[hashed_key][1]
            hashed_key = (hashed_key + 1) % self.capacity
            if hashed_key == start_index:
                break
        return -1

    def remove(self, key: int) -> bool:
        hashed_key = self._hash(key)
        start_index = hashed_key
        while self.array[hashed_key] is not None:
            if self.array[hashed_key][0] == key:
                self.array[hashed_key] = None
                self.length -= 1
                # Rehash elements in the same cluster to maintain linear probing integrity
                next_idx = (hashed_key + 1) % self.capacity
                while self.array[next_idx] is not None:
                    node_to_rehash = self.array[next_idx]
                    self.array[next_idx] = None
                    self.length -= 1
                    self.insert(node_to_rehash[0], node_to_rehash[1])
                    next_idx = (next_idx + 1) % self.capacity
                return True
            hashed_key = (hashed_key + 1) % self.capacity
            if hashed_key == start_index:
                break
        return False

    def getSize(self) -> int:
        return self.length

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        old_array = self.array
        self.capacity *= 2
        self.array = [None] * self.capacity
        self.length = 0
        for item in old_array:
            if item:
                self.insert(item[0], item[1])