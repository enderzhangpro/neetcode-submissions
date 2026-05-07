class MinHeap:
    
    def __init__(self):
        self.heap = []

    def push(self, val: int) -> None:
        self.heap.append(val)
        index = len(self.heap) - 1
    
        while index > 0 and self.heap[(index - 1) // 2] > self.heap[index]:
            self.heap[index], self.heap[(index - 1) // 2] = self.heap[(index - 1) // 2], self.heap[index]
            index = (index - 1) // 2


    def pop(self) -> int:
        if len(self.heap) == 0:
            return -1
        if len(self.heap) == 1:
            return self.heap.pop()
        returnVal = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._siftDown(0)
        return returnVal


    def top(self) -> int:
        if len(self.heap) == 0:
            return -1
        return self.heap[0]


    def heapify(self, nums: List[int]) -> None:
        self.heap = nums
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._siftDown(i)
            
    def _siftDown(self, index):
        while index * 2 + 1 < len(self.heap):
            smallest = index * 2 + 1
            if smallest + 1 < len(self.heap) and self.heap[smallest + 1] < self.heap[smallest]:
                smallest += 1
            if self.heap[index] <= self.heap[smallest]:
                break
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest