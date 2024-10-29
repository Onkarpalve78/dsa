
from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def inOrderTraversal(self, root, arr):
        if root is None:
            return

        self.inOrderTraversal(root.left, arr)
        arr.append(root.value)
        self.inOrderTraversal(root.right, arr)

    def preOrderTraversal(self, root, arr):
        if root is None:
            return

        arr.append(root.value)
        self.preOrderTraversal(root.left, arr)
        self.preOrderTraversal(root.right, arr)

    def postOrderTraversal(self, root, arr):
        if root is None:
            return

        self.postOrderTraversal(root.left, arr)
        self.postOrderTraversal(root.right, arr)

        arr.append(root.value)

    def breadthFirstSearch(self, root, arr):
        if not root:
            return root

        queue = deque()
        queue.append(root)

        while queue:
            level = []
            size = len(queue)

            for i in range(size):
                node = queue.popleft()
                level.append(node.value)

                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)

            arr.append(level)


btree = BinaryTree(1)

btree.root.left = Node(2)
btree.root.right = Node(3)

btree.root.left.left = Node(4)
btree.root.left.right = Node(5)

preorder = []
btree.preOrderTraversal(btree.root, preorder)
print(preorder)

inorder = []
btree.inOrderTraversal(btree.root, inorder)
print(inorder)

postorder = []
btree.postOrderTraversal(btree.root, postorder)
print(postorder)

bfs = []
btree.breadthFirstSearch(btree.root, bfs)
print(bfs)
