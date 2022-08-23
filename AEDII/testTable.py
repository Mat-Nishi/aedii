from table import Table

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