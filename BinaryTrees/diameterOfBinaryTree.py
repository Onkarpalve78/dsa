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


# Here we check the maximum number of paths between two nodes, path doesnt need to be from the root node

def diameterOfBtree(root: Node, diameter):
    if not root:
        return 0

    lh = diameterOfBtree(root.left, diameter)
    rh = diameterOfBtree(root.right, diameter)

    diameter = max(diameter, lh+rh)

    return 1+max(lh, rh)


diameter = 0
print(diameterOfBtree(tree.root, diameter))
