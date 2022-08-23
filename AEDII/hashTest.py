from hash import Hash

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