class Hash:
    def __init__(self, size) -> None:
        self._max = size
        self._values = [None]*self._max
        self._keys = [None]*self._max
        self._link = [None]*self._max
        self._len = 0

    def __repr__(self) -> str:
        return f"HashTable(size)"
    
    def __str__(self) -> str:
        out = ""
        for val, key in self:
            out += f"{str(key)}: {str(val)}\n"
        return out[:-1] if out else "Empty"

    def __iter__(self):
        for i in range(len(self._keys)):
            if self._keys[i] is not None:
                yield self._values[i], self._keys[i]

    def __len__(self) -> int:
        return self._len

    def isEmpty(self) -> bool:
        # returns True if there are no items in table, else returns false
        return False if len(self) else True

    def isFull(self) -> bool:
        # returns True if table has a number of items equal to the limit, else returns false
        return True if len(self) == self._max else False

    def _hash(self, key):
        # encodes key as index position and returns it
        if type(key) == str:
            # converts string into int by adding ascii value of each char
            idx = 0
            for char in key:
                idx += ord(char)
        else:
            try:
                idx = int(key)
            except:
                raise KeyError("Key must be a number or string value")

        return idx%self._max

    def insert(self, key, value):
        if self.isFull():
            raise IndexError("Cannot insert in full table")

        idx = firstIdx = self._hash(key)
        while self._keys[idx] is not None and self._keys[idx] != key:
            # colision handling (linear search)
            if self._link[idx] is not None:
                idx = (self._link[idx] + 1) % self._max
            else:
                idx = (idx+1)%self._max

        self._keys[idx] = key
        self._values[idx] = value
        if idx != firstIdx:
            self._link[firstIdx] = idx
        self._len += 1

    def remove(self, key):
        # removes key value pair from table if it exists
        # returns 1 if removed else 0
        idx = self._hash(key)
        while self._keys[idx] != key:
            if self._link[idx] is not None:
                idx = self._link[idx] 
            else: return 0
        self._keys[idx] = self._values[idx] = None
        self._len -= 1
        return 1    

    def getValue(self, key):
        # returns value of given key if present, else returns None type
        idx = self._hash(key)
        while self._keys[idx] != key:
            if self._link[idx] is not None:
                idx = self._link[idx] 
            else: return None
        return self._values[idx]

    def getKey(self, value):
        # returns key of first occurance of given value, if value is not present returns None type
        for i in range(len(self._values)):
            if value == self._values[i]:
                return self._keys[i]
        return None

    def clear(self):
        self._values = [None]*self._max
        self._keys = [None]*self._max
        self._link = [None]*self._max
        self._len = 0

def main():
    myTable = Hash(10)
    
    keys = [21, 31, 41, 0, 10, 9]
    c = 1
    for key in keys:
        myTable.insert(key, c)
        c += 1
    print(myTable)
    print(f"lenght of table is: {len(myTable)}")
    print()
    print("---removing items---")
    myTable.remove(21)
    myTable.remove(9)
    print(myTable)
    print(f"lenght of table is: {len(myTable)}")
    print()
    print("---adding more items---")
    myTable.insert(81, 1)
    myTable.insert(50, 6)
    print(myTable)
    print(f"lenght of table is: {len(myTable)}")
    print()

    print("---searching a key---")
    print('81 =', myTable.getValue(81))

    print("---searching a non existant key---")
    print('7 =', myTable.getValue(7))

    print()
    print("---destroying table---")
    myTable.clear()
    print(myTable)
    print(f"lenght of table is: {len(myTable)}")

if __name__ == "__main__":
    main()