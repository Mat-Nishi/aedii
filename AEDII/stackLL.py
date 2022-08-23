class Node:
    def __init__(self, val, next=None) -> None:
        self._data = val
        self._next = next

    def __repr__(self) -> str:
        return f"Node({self._data})"

    def __str__(self) -> str:
        return str(self._data)

class Stack:
    def __init__(self, *vals) -> None:
        data = [Node(i) for i in vals]
        self._len = len(data)
        for i in range(self._len-1, 0, -1):
            data[i]._next = data[i-1]
        
        if self._len:
            self._head = data[-1]
        else:
            self._head = None

    def __repr__(self) -> str:
        return "Stack()"

    def __str__(self) -> str:
        if self._len == 0:
            return "[]"
        out = "["
        vals = []
        cur = self._head
        while cur:
            vals.append(cur._data)
            cur = cur._next
        vals.reverse()
        for val in vals:
            out += f"{val}, "
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
    
    def top(self):
        if not self._isEmpty():
            return self._head._data
        return None

    def add(self, *vals):
        for i in range(len(vals)):
            cur = self._head
            self._head = Node(vals[i], cur)
        self._len += len(vals)

    def pop(self):
        if self._isEmpty():
            raise IndexError("Cannot remove from empty stack")
        self._head = self._head._next
        self._len -= 1

    def remove(self, n):
        if self._len < n:
            raise IndexError(f"Stack does not contain {n} items to remove")
        for i in range(n):
            self._head = self._head._next
        self._len -= n

    def clear(self):
        self._len = 0
        self._head = None

def main():
    print("Testing:")
    stack = Stack(1,2,3,4)
    print(f"Creating a stack -> {stack}")
    print("Adding numbers 6 then 5 to the stack:")
    stack.add(6)
    stack.add(5)
    print(stack)
    print("Removing three elements from the stack:")
    stack.pop()
    stack.remove(2)
    print(stack)
    print(f"Length of the stack is -> {len(stack)}")
    stack.add(8, 17, 36)
    print("Adding 8 then 17 then 36:")
    print(stack)
    print(f"Top element is -> {stack.top()}")
    print("Removing all elements:")
    stack.clear()
    print(stack)
    print(f"Top element is -> {stack.top()}")

if __name__ == "__main__":
    main()