class MinStack:

    def __init__(self):
        self.stack = []
        self.prefix = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.prefix) > 0:
            self.prefix.append(min(val, self.prefix[-1]))
        else:
            self.prefix.append(val)

    def pop(self) -> None:
        popped = self.stack[-1]
        del self.stack[-1]
        del self.prefix[-1]
        return popped

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.prefix[-1]
