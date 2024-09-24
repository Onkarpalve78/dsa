

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


firstNode = BinaryTreeNode(1)
firstNode.left = BinaryTreeNode(2)
firstNode.right = BinaryTreeNode(3)

firstNode.left.left = BinaryTreeNode(4)
firstNode.left.right = BinaryTreeNode(5)

# The structure of the tree is:
#       1
#      / \
#     2   3
#    / \
#   4   5

print(firstNode.left.left.value)
print(firstNode.left.right.value)
