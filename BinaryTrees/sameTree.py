# LC 100 https://leetcode.com/problems/same-tree/description/
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
from BinaryTree import BinaryTree, Node

tree = BinaryTree(1)

tree.root.left = Node(2)
tree.root.right = Node(3)

tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

tree.root.left.left.left = Node(6)
tree.root.left.right.left = Node(7)


tree2 = BinaryTree(1)

tree2.root.left = Node(2)
tree2.root.right = Node(3)

tree2.root.left.left = Node(4)
tree2.root.left.right = Node(5)

tree2.root.left.left.left = Node(6)
tree2.root.left.right.left = Node(7)


def sameTree(root1, root2):
    # If both nodes are None, they are the same
    if not root1 and not root2:
        return True

    # If one of the nodes is None, they are not the same
    if not root1 or not root2:
        return False

    # If the values of the nodes are different, they are not the same
    if root1.value != root2.value:
        return False

    # Recursively check the left and right subtrees
    return sameTree(root1.left, root2.left) and sameTree(root1.right, root2.right)


print(sameTree(tree.root, tree2.root))
