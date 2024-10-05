from collections import deque


class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree():
    def __init__(self, root) -> None:
        self.root = Node(root)

    def preOrderTraversal(self, root, arr):
        if root is None:
            return
        arr.append(root.value)

        self.preOrderTraversal(root.left, arr)
        self.preOrderTraversal(root.right, arr)

    def inOrderTraversal(self, root, arr):
        if root is None:
            return
        self.inOrderTraversal(root.left, arr)

        arr.append(root.value)

        self.inOrderTraversal(root.right, arr)

    def postOrderTraversal(self, root, arr):
        if root is None:
            return

        self.postOrderTraversal(root.left, arr)
        self.postOrderTraversal(root.right, arr)

        arr.append(root.value)

    def breathFirstSearch(self, root, arr):
        if not root:
            return arr  # return 0 if you only want to find height of binary tree

        queue = deque()
        queue.append(root)

        while queue:
            level = []
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()
                level.append(node.value)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            arr.append(level)

    def heightOfBtee(self, root):
        if root is None:
            return 0

        left_height = self.heightOfBtee(root.left)
        right_height = self.heightOfBtee(root.right)

        return 1+max(left_height, right_height)

    def diameterOfBtree(self, root):
        if root is None:
            return 0, 0

        left_height, left_diameter = self.diameterOfBtree(root.left)
        right_height, right_diameter = self.diameterOfBtree(root.right)
        current_diameter = left_height+right_height

        return 1+max(left_height, right_height), max(left_diameter, right_diameter, current_diameter)

    #  the height difference between left and right subtrees is at most 1 for every node
    def isBtreeBalanced(self, root):
        if root is None:
            return 0, True

        lh, l_balanced = self.isBtreeBalanced(root.left)
        rh, r_balanced = self.isBtreeBalanced(root.right)

        balanced = abs(lh-rh) <= 1

        return 1+max(lh, rh), balanced and l_balanced and r_balanced

    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        print(f"Visiting Node {root.value if root else 'None'}, returning {root.value if (left and right) else (left.value if left else (right.value if right else 'None'))}")

        return left if left else right


tree = BinaryTree(1)

tree.root.left = Node(2)
tree.root.right = Node(3)

tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

tree.root.left.left.left = Node(6)
tree.root.left.right.left = Node(7)

preorder = []
tree.preOrderTraversal(tree.root, preorder)
print(preorder)

inorder = []
tree.inOrderTraversal(tree.root, inorder)
print(inorder)

postorder = []
tree.postOrderTraversal(tree.root, postorder)
print(postorder)

bfs = []
tree.breathFirstSearch(tree.root, bfs)
treeHeight = len(bfs)
print(bfs, "height: ", treeHeight)


h = tree.heightOfBtee(tree.root)
print(h)

diameter = tree.diameterOfBtree(tree.root)
print(diameter[1])

balanced = tree.isBtreeBalanced(tree.root)
print(balanced[1])

lnode = 2
rnode = 3
lca = tree.lowestCommonAncestor(tree.root, lnode, rnode)
print(lca)

# The structure of the tree is:
#       1
#      / \
#     2   3
#    / \
#   4   5
