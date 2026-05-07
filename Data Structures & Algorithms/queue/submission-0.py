class Node:

    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


    def isEmpty(self) -> bool:
        if self.length == 0:
            return True
        return False
        

    def append(self, value: int) -> None:
        newNode = Node(value, self.tail, None)
        if self.tail:
            self.tail.next = newNode
        self.tail = newNode
        if self.head is None:
            self.head = self.tail
        self.length += 1
        

    def appendleft(self, value: int) -> None:
        newNode = Node(value, None, self.head)
        if self.head:
            self.head.prev = newNode
        self.head = newNode
        if self.tail is None:
            self.tail = self.head
        self.length += 1
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        returnValue = self.tail.value
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None
        self.length -= 1
        return returnValue
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        returnValue = self.head.value
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        self.length -= 1
        return returnValue
        
