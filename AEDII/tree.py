class Node:
    def __init__(self, value, left=None, right=None):
        self._value = value
        self._left = left
        self._right = right

    def __str__(self):
        return "node "+str(self._value)

    def __repr__(self):
        return "Node(value)"

class BinaryTree:
    def __init__(self, root):
        self._root = Node(root)

    def __str__(self):
        return str(self.get_nodes(self._root))

    def __len__(self):
        return len(self.get_nodes(self._root))

    def __repr__(self):
        return "BinaryTree(root)"

    def get_nodes(self, root):
        x = []
        if root is not None:
            x = self.get_nodes(root._left)
            x.append(root._value)
            x = x + self.get_nodes(root._right)
        return x

    def dfs_insert(self, val, root=None):
        if root == None: root = self._root
        if root._value == val:
            return root

        left = root._left
        right = root._right

        if left is not None:
            x = self.dfs_insert(val, left)
            if x is not None: return x 

        if right is not None:
            x = self.dfs_insert(val, right)
            if x is not None: return x 

    def insert(self, val, father, pos=0): # pos> 0 = left, 1 = right
        # returns 0 if failed to insert
        node = Node(val)
        if father == None and self._root == None: 
            self._root = Node(val)
            return 1

        father = self.dfs_insert(father)
        if father is None: return 0 # father value not found

        if not pos:
            if father._left is not None: return 0 #position already ocupied
            else: father._left = node
            return 1

        if father._right is not None: return 0 #position already ocupied
        else: father._right = node
        return 1

    def dfs_remove(self, val, root=None):
        if root == None: root = self._root
        if root._left is not None and root._left._value == val:
            return root
        if root._right is not None and root._right._value == val:
            return root

        left = root._left
        right = root._right

        if left is not None:
            x = self.dfs_remove(val, left)
            if x is not None: return x 

        if right is not None:
            x = self.dfs_remove(val, right)
            if x is not None: return x 

    def remove(self, val): # returns 1 if value was removed, otherwise 0
        if val == self._root._value:
            self._root = None
            return 1
        father = self.dfs_remove(val)
        if father is None: return 0

        if father._left._value == val:
            father._left = None
            return 1
        
        father._right = None
        return 1

def main():
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

if __name__=="__main__":
    main()