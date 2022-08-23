class Table:
    def __init__(self, size) -> None:
        self._max = size
        self._values = [None]*self._max
        self._keys = [None]*self._max
        self._end = -1

    def __repr__(self) -> str:
        return f"Table(size)"
    
    def __str__(self) -> str:
        out = ""
        for val, key in self:
            out += f"{str(key)}: {str(val)}\n"
        return out[:-1] if out else "Empty"

    def __iter__(self):
        i = 0
        while self._keys[i] is not None:
            yield self._values[i], self._keys[i]
            i += 1

    def __len__(self) -> int:
        return self._end + 1 if self._end>-1 else 0

    def isEmpty(self) -> bool:
        # returns True if there are no items in table, else returns false
        return False if len(self) else True

    def isFull(self) -> bool:
        # returns True if table has a number of items equal to the limit, else returns false
        return True if len(self) == self._max else False

    def insert(self, key, value):
        # returns 0 if key's value was updated or 1 if new key was created
        if self.isFull():
            raise IndexError("Cannot insert in full table")

        # updates value if key is already in use
        for i in range(len(self)):
            if key == self._keys[i]:
                self._keys[i] = key
                self._values[i] = value
                return 0

        # otherwise, creates a new key to store the value
        self._end += 1
        self._keys[self._end] = key
        self._values[self._end] = value
        return 1

    def orderedInsert(self, key, value):
        # returns 0 if key's value was updated or 1 if new key was created
        if self.isFull():
            raise IndexError("Cannot insert in full table")

        for i in range(len(self)):
            if key > self._keys[i]:
                # searching for index to insert
                continue
            elif key == self._keys[i]:
                # if key already exists, update its value
                self._keys[i] = key
                self._values[i] = value
                return 0
            else:
                # found index to insert
                idx = i
                break
        else:
            # insert at the end if given key is bigger than all currently stored keys
            self._end += 1
            self._keys[self._end] = key
            self._values[self._end] = value
            return 1
        
        for i in range(len(self), idx-1, -1):
            # clear space at found index for insertion
            self._keys[i] = self._keys[i-1]
            self._values[i] = self._values[i-1]
        self._keys[idx] = key
        self._values[idx] = value
        self._end += 1
        return 1

    def remove(self, key):
        # returns False if key was not in table
        if self.isEmpty():
            raise IndexError("Cannot remove from empty table")

        found = False
        for i in range(len(self)):
            if self._keys[i] == key or found:
                found = True
                try:
                    self._keys[i] = self._keys[i+1]
                    self._values[i] = self._values[i+1]
                except IndexError:
                    self._keys[i] = None
                    self._values[i] = None
        if not found:
            return False
        else:
            self._end -= 1
            return True

    # Iterative Method
    # def linearSearchKey(self, key):
    #     # returns None if key is not in table
    #     for val, k in self:
    #         if k == key:
    #             return val
    #     return None

    # Recursive Method
    def linearSearchKey(self, key, cur=0):
        if cur >= len(self): return None
        if self._keys[cur] == key:
            return self._values[cur]
        return self.linearSearchKey(key, cur+1)

    # Iterative Method
    # def binarySearchKey(self, key):
    #     # returns None if key is not in table
    #     min = 0
    #     max = len(self)-1
    #     cur = 0

    #     while cur <= max:
    #         cur = (max+min)//2

    #         if self._keys[cur] > key:
    #             # value is in left half of checked subarray
    #             max = cur
    #         elif self._keys[cur] < key:
    #             # value is in right half of checked subarray
    #             min = cur+1
    #         else:
    #             # found the value
    #             return self._values[cur]
    #     return None

    def binarySearchKey(self, key, min=0, max=None):
        if max==None: max = len(self)

        if max >= min:
            mid = (min+max)//2
            if self._keys[mid] == key:
                return self._values[mid]
            elif self._keys[mid] > key:
                return self.binarySearchKey(key, min, mid)
            else:
                return self.binarySearchKey(key, mid+1, max)

        return None

    def getValue(self, key, opt='linear'):
        if opt == 'linear':
            return self.linearSearchKey(key)
        elif opt == 'binary':
            return self.binarySearchKey(key)

    def getKey(self, value):
        # returns key of first occurance of given value
        for val, key in self:
            if val == value:
                return key
        return None

    def clear(self):
        self._values = [None]*self._max
        self._keys = [None]*self._max
        self._end = -1

def main():
    myTable = Table(10)
    
    keys = 'efweaweg'
    for char in keys:
        myTable.orderedInsert(char, [ord(char), ord(char)//3, chr(ord(char)+4)])
    print(myTable)
    print(f"lenght of table is: {len(myTable)}")
    print()
    print("---removing items---")
    myTable.remove('f')
    myTable.remove('w')
    print(myTable)
    print(f"lenght of table is: {len(myTable)}")
    print()
    print("---adding more items in order---")
    myTable.orderedInsert('f',[12,56,3])
    myTable.orderedInsert('h',[25,65,78])
    myTable.orderedInsert('r',[165,521,2])
    myTable.orderedInsert('y',[11,76,3])
    myTable.orderedInsert('o',[126,91,16])
    print(myTable)
    print(f"lenght of table is: {len(myTable)}")
    print()

    print("---binary searching a key---")
    print('o =', myTable.getValue('o', 'binary'))

    print("---linear searching a key---")
    print('h =', myTable.getValue('h'))

    print()
    print("---destroying table---")
    myTable.clear()
    print(myTable)
    print(f"lenght of table is: {len(myTable)}")

if __name__ == "__main__":
    main()