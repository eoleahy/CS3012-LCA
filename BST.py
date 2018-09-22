class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

class Tree:

    def __init__(self):
        self.root = None
        self.size = 0

    def getRoot(self):
        return self.root

    def insert(self, val):
        if(self.root == None):
            self.root = Node(val)
        else:
            self._insert(val, self.root)

    def _insert(self, val, node):
        if(val < node.val):
            if(node.left != None):
                self._insert(val, node.left)
            else:
                node.left = Node(val)
        else:
            if(node.right != None):
                self._insert(val, node.right)
            else:
                node.right = Node(val)
