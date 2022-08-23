from tree import BinaryTree

tree = BinaryTree(1)
tree.insert(2,1)
tree.insert(3,1,1)
print(tree)
tree.insert(4,2)
tree.insert(5,2,1)
tree.insert(6,3)
tree.insert(7,3,1)
tree.insert(8,4)
tree.insert(9,4,1)
tree.insert(10,5)
tree.insert(11,5,1)
tree.insert(12,6)
tree.insert(13,6,1)
tree.insert(14,7)
tree.insert(15,7,1)

print(tree)

tree.remove(2)
print(tree)
