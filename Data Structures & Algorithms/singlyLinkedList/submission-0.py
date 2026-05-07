class LinkedList:
    
    def __init__(self):
        self.array = []

    
    def get(self, index: int) -> int:
        if index >= len(self.array):
            return -1
        return self.array[index]
        

    def insertHead(self, val: int) -> None:
        self.array.insert(0, val)
        

    def insertTail(self, val: int) -> None:
        self.array.append(val)
        

    def remove(self, index: int) -> bool:
        if index >= len(self.array):
            return False
        self.array.pop(index)
        return True
        

    def getValues(self) -> List[int]:
        return self.array
        
