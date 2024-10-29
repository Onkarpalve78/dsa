from BinaryTree import Node, BinaryTree
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


def bottomView(root: Node):
    if not root:
        return []

    level_map = {}

    queue = deque()
    queue.append((root, 0))

    while queue:
        node, level = queue.popleft()

        level_map[level] = node.value

        if node.left:
            queue.append((node.left, level-1))
        if node.right:
            queue.append((node.right, level+1))

    bottom_view = [level_map[key] for key in sorted(level_map)]
    return bottom_view


print(bottomView(tree.root))
