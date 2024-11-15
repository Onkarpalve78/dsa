from BinaryTree import BinaryTree, Node
from collections import deque
tree = BinaryTree(1)

tree.root.left = Node(2)
tree.root.right = Node(3)

tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

tree.root.left.left.left = Node(6)
tree.root.left.right.left = Node(7)

# The structure of the tree is:
#       1
#      / \
#     2   3
#    / \
#   4   5
#  /   /
# 6   7


def maxHeight(root: Node):
    if not root:
        return 0

    lh = maxHeight(root.left)
    rh = maxHeight(root.right)

    return 1+max(lh, rh)


print(maxHeight(tree.root))
