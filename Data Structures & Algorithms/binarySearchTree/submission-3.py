class Node:

    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
    
    def numChildren(self):
        num = 0
        if self.left:
            num += 1
        if self.right:
            num += 1
        return num

class TreeMap:
    
    def __init__(self):
        self.root = None


    def insert(self, key: int, val: int) -> None:
        if self.root is None:
            self.root = Node(key=key, val=val)
        else:
            parent = None
            current = self.root
            while current is not None:
                if current.key == key:
                    current.val = val
                    return
                elif current.key < key:
                    parent = current
                    current = current.right
                else:
                    parent = current
                    current = current.left
            current = Node(key=key, val=val)
            if parent.key < key:
                parent.right = current
            else:
                parent.left = current


    def get(self, key: int) -> int:
        current = self.root
        while current is not None:
            if current.key == key:
                return current.val
            elif current.key < key:
                current = current.right
            else:
                current = current.left
        return -1


    def getMin(self) -> int:
        if self.root is None:
            return -1
        current = self.root
        while current.left is not None:
            current = current.left
        return current.val


    def getMax(self) -> int:
        if self.root is None:
            return -1
        current = self.root
        while current.right is not None:
            current = current.right
        return current.val


    def remove(self, key: int) -> None:
        if self.root is None:
            return
        parent = None
        current = self.root
        while current is not None:
            if current.key == key:
                break
            elif current.key < key:
                parent = current
                current = current.right
            else:
                parent = current
                current = current.left
        if current is None:
            return
        if current.numChildren() == 0:
            if parent is None:
                self.root = None
            elif parent.key < current.key:
                parent.right = None
                current = None
            else:
                parent.left = None
                current = None
        elif current.numChildren() == 1:
            if current.left:
                child = current.left
            else:
                child = current.right
            if parent is None:
                self.root = child
            elif parent.key < current.key:
                parent.right = child
            else:
                parent.left = child
        else:
            replacement_parent = current
            replacement = current.right
            while replacement.left is not None:
                replacement_parent = replacement
                replacement = replacement.left
            current.key = replacement.key
            current.val = replacement.val
            
            child = replacement.right
            if replacement_parent.left == replacement:
                replacement_parent.left = child
            else:
                replacement_parent.right = child


    def getInorderKeys(self) -> List[int]:
        keys = []
        def traversal(node):
            if node is None:
                return
            if node.left:
                traversal(node.left)
            keys.append(node.key)
            if node.right:
                traversal(node.right)
        traversal(self.root)
        return keys
