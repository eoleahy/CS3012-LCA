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

    def isEmpty(self):
        return self.root is None

    def insert(self, val):
        if(self.isEmpty()):
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

    def findPath(self,root, path, value):
        if root is None:
            return False

        path.append(root.val)

        if(root.val ==value):
            return True

        if((root.left != None and self.findPath(root.left, path, value)) or
            (root.right != None and self.findPath(root.right, path, value))):
            return True

        path.pop()
        return False

    def lca(self,root, valA, valB):

        pathA =[]
        pathB =[]

        if(not self.findPath(self.root, pathA, valA) or not self.findPath(self.root, pathB, valB)):
            return -1

        i=0
        while(i<len(pathA) and i< len(pathB)):
            if(pathA[i] != pathB[i]):
                break
            i+= 1

        return pathA[i-1]
