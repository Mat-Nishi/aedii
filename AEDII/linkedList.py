class Node:
    # Node class for implementing linked list
    def __init__(self, val, next=None, prev=None):
        self._data = val
        self._next = next
        self._prev = prev
    
    def __repr__(self):
        return "Node(val, next)"

    def __str__(self):
        return f"Node({self._data})"

class LinkedList:
    # Linked list constructor, starts with 0 or more values
    # Stores head node and tail node of given Linked List
    def __init__(self, *nodes):
        self._len = len(nodes)
        if self._len:
            data = []
            for i in range(self._len):
                data.append(Node(nodes[i]))
            for i in range(self._len - 1):
                data[i]._next = data[i+1]
            for i in range(1, self._len):
                data[i]._prev = data[i-1]
            self._head = data[0]
            self._tail = data[-1]
        else:
            self._head = self._tail = None

    def __repr__(self) -> str:
        return "LinkedList(*nodes)"

    def __str__(self) -> str:
        out = ""
        for node in self:
            out += f"{str(node._data)}, "
        return f"[{out[:-2]}]"

    def __iter__(self):
        cur = self._head
        while cur:
            yield cur
            cur = cur._next

    def __len__(self):
        return self._len

    @staticmethod
    def isEqual(list1, list2):
        node1 = list1._head
        node2 = list2._head
        val1 = node1._data
        val2 = node2._data
        while True:
            try:
                val1 = node1._data
            except AttributeError:
                val1 = None
            try:
                val2 = node2._data
            except AttributeError:
                val2 = None
            if val1 != val2:
                return False
            if val1 == val2 == None:
                return True
            node1 = node1._next
            node2 = node2._next

    def isEmpty(self):
        # Returns True if list contains no nodes
        return not self._len

    def append(self, val):
        # Appends value at the end (as tail) of linked list, returns new length of list
        node = Node(val, prev=self._tail)
        if self.isEmpty():
            self._head = self._tail = node
            self._len += 1
            return self._len

        self._tail._next = node
        self._tail = node
        self._len += 1
        return self._len

    def insert(self, val, idx):
        # Inserts given value at given index, returns new length of list
        if idx >= self._len:
            raise IndexError("Index is out of range.\nIf you are trying to add a value to the last position use .add() function instead")

        if idx < 0:
            idx = self._len + idx + 1

        if idx == 0:
            node = Node(val, self._head)
            self._head._prev = node
            self._head = node
            self._len += 1
            return self._len

        cur = self._head
        count = 1
        while count < idx:
            cur = cur._next
            count += 1

        newNext = cur._next
        node = Node(val, newNext, cur)
        cur._next = node
        self._len += 1
        return self._len

    def pop(self, idx=-1):
        # Removes node at given index, removes last node by default. Returns new length of list
        if idx >= self._len:
            raise IndexError("Index is out of range.")

        if idx < 0:
            idx = self._len + idx
        
        cur = self._head

        if idx == 0:
            self._head = cur._next
            cur._prev = None
            self._len -= 1
            return self._len

        count = 1
        while count < idx:
            cur = cur._next
            count += 1

        if idx == self._len - 2:
            self._tail = cur
            cur._next = None
            self._len -= 1
            return self._len

        newNext = cur._next._next 
        if newNext:
            newNext._prev = cur

        cur._next = newNext
        self._len -= 1
        return self._len

    # Iterative method
    # def getValue(self, idx):
    #     if idx >= self._len:
    #         raise IndexError("Index is out of range.")

    #     cur = self._head
    #     count = 0
    #     while count < idx:
    #         cur = cur._next
    #         count += 1

    #     return cur._data

    # Recursive method
    def getValue(self, idx, cur=None):
        if idx >= len(self): raise IndexError("Index is out of range")
        cur = self._head if cur is None else cur._next
        if idx == 0:
            return cur._data

        return self.getValue(idx-1, cur)

    def indexOf(self, val):
        # Returns index of first occurence of given value, returns None if value not in list.
        cur = self._head
        count = 0
        while cur:
            if cur._data == val:
                return count
            cur = cur._next
            count+= 1

        return None

    def clear(self):
        # Empties the list
        self._head = None
        self._tail = None

    def reverse(self):
        # Reverses list
        cur = self._head
        next = self._head._next
        self._head = self._tail
        self._tail = cur
        cur._next = None
        while next:
            prev = cur
            cur = next
            next = cur._next
            cur._next = prev

def main():
    myList = LinkedList(0, 1, 2)
    secondList = LinkedList(0, 1, 2, 3, 4, 5, 6, 7)
    thirdList = LinkedList(0, 1, 2, 3, 4, 9, 6, 7)
    myList.append(5)
    myList.append(7)
    myList.insert(4, 3)
    myList.insert(3, 3)
    myList.insert(6, 6)
    print(f"Linked list -> {myList}")
    print(f"Length of linked list is: {len(myList)}")
    print(f"Index of value 4 is: {myList.indexOf(4)}")
    print(f"Value at index 2 is: {myList.getValue(2)}")

    # Checking if lists are equal
    print(f"Is myList == secondList? {LinkedList.isEqual(myList, secondList)}")
    print(f"Is myList == thirdList? {LinkedList.isEqual(myList, thirdList)}")

    myList.reverse()
    print(f"Reversed linked list -> {myList}")
    myList.pop()
    myList.pop(0)
    myList.pop(3)
    myList.pop(4)
    print(f"List after pop -> {myList}")
    myList.clear()
    print(myList)
    

if __name__ == "__main__":
    main()
