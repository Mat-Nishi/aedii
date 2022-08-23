from stack import Node, Stack

class Queue:
    def __init__(self, *vals):
        data = [Node(i) for i in vals]
        self._len = len(data)
        for i in range(0, self._len-1):
            data[i]._next = data[i+1]
        
        if self._len:
            self._head = data[0]
            self._tail = data[-1]
        else:
            self._head = None
            self._tail = None

    def __repr__(self) -> str:
        return "Queue()"

    def __str__(self) -> str:
        if self._len == 0:
            return "[]"
        out = "["
        for val in self:
            if val:
                out += f"{val._data}, "
        return out[:-2] + "]"
    
    def __len__(self) -> int:
        return self._len
    
    def __iter__(self):
        cur = self._head
        while cur:
            yield cur
            cur = cur._next
    
    def _isEmpty(self):
        if self._len == 0:
            return True
        return False
        
    def add(self, *vals):
        if not len(vals): return
        data = [Node(i) for i in vals]
        
        if self._len == 0:
            self._len = len(data)
            for i in range(0, self._len-1):
                data[i]._next = data[i+1]
            self._head = data[0]
            self._tail = data[-1]
            return

        for i in range(len(data)):
            self._tail._next = data[i]
            self._tail = data[i]
        self._len += len(data)
        
    def pop(self):
        self._head = self._head._next
        self._len -= 1

    def remove(self, n):
        for _ in range(n):
            self.pop()

    def clear(self):
        self._head = None
        self._tail = None
        self._len = 0

    def front(self):
        return self._head._data

    def stackSort(self):
        ordStack = Stack()
        auxStack = Stack()

        while(self._len):
            if (not len(ordStack)) or ordStack.top() >= self.front():
                ordStack.add(self.front())
                self.pop()
            else:
                while len(ordStack) and ordStack.top() < self.front():
                    auxStack.add(ordStack.top())
                    ordStack.pop()
                ordStack.add(self.front())
                self.pop()
                while(len(auxStack)):
                    ordStack.add(auxStack.top())
                    auxStack.pop()

        while(len(ordStack)):
            self.add(ordStack.top())
            ordStack.pop()

def main():
    queue = Queue(4,6,2,5,74,21,3,54)
    print(queue)
    queue.stackSort()
    print(queue)

if __name__ == "__main__":
    main()