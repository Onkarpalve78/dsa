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


def maxWidthOfBtree(root: Node):
    if not root:
        return 0

    ans = 0
    queue = deque()
    queue.append([root, 1, 0])

    prevLevel, firstNodePositionOfLevel = 0, 1

    while queue:
        node, num, level = queue.popleft()

        if level > prevLevel:
            prevLevel = level
            firstNodePositionOfLevel = num

        ans = max(ans, (num-firstNodePositionOfLevel)+1)

        if node.left:
            queue.append([node.left, num*2, level+1])

        if node.right:
            queue.append([node.right, num*2+1, level+1])

    return ans


print("Width: ", maxWidthOfBtree(tree.root))
