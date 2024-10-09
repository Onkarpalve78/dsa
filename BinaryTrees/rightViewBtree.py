

class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree():
    def __init__(self, root):
        self.root = Node(root)

    def leftView(self, root, level, arr):
        if root is None:
            return

        if level == len(arr):
            arr.append(root.val)

        if root.left:
            self.leftView(root.left, level+1, arr)
        if root.right:
            self.leftView(root.right, level+1, arr)

    def rightView(self, root, level, arr):
        if root is None:
            return

        if level == len(arr):
            arr.append(root.val)

        if root.right:
            self.rightView(root.right, level+1, arr)
        if root.left:
            self.rightView(root.left, level+1, arr)


btree = BinaryTree(1)
btree.root.left = Node(2)
btree.root.right = Node(3)

btree.root.left.left = Node(4)

lview = []
btree.leftView(btree.root, 0, lview)
print("Left view: ", lview)

rview = []
btree.rightView(btree.root, 0, rview)
print("Right view: ", rview)
