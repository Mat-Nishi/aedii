class Stack:
    def __init__(self, size, *vals):
        self._data = list(vals)
        self._len = len(vals)
        self._max = size-1
        for _ in range(size-self._len):
            self._data.append(None)

    def __repr__(self) -> str:
        return(f"Stack({self._max+1})")

    def __str__(self) -> str:
        if self._len == 0:
            return "[]"
        out = "["
        for val in self._data:
            if val:
               out += str(val) + ", "  
        return out[:-2] + "]"

    def __len__(self):
        return self._len

    def __iter__(self):
        for i in self._data:
            if i:
                yield i
        
    def _isEmpty(self):
        if self._len == 0:
            return True
        return False

    def top(self):
        if not self._isEmpty():
            return self._data[self._len - 1]
        return None
    
    def pop(self):
        if self._isEmpty():
            raise IndexError("Cannot remove from empty stack")
        self._data[self._len-1] = None
        self._len -= 1

    def remove(self, n):
        if self._len < n:
            raise IndexError(f"Stack does not contain {n} items to remove")
        for i in range(self._len-n, self._len):
            self._data[i] = None
        self._len -= n
 
    def add(self, *vals):
        if not len(vals): return
        if self._len + len(vals) > self._max:
            raise IndexError("Stack is already full")
        for i in range(len(vals)):
            self._data[self._len+i] = vals[i]
        self._len += len(vals)

    def clear(self):
        self._len = 0
        self._data = [None for _ in range(self._max+1)]

def main():
    print("Testing:")
    stack = Stack(10, 1,2,3,4)
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