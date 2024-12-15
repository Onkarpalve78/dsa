from BinaryTree import BinaryTree, Node
from collections import deque
tree = BinaryTree(1)

tree.root.left = Node(2)
tree.root.right = Node(3)

tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

tree.root.left.left.left = Node(6)
tree.root.left.right.left = Node(7)
tree.root.left.right.right = Node(8)
tree.root.left.right.right.left = Node(9)

# The structure of the tree is:
#       1
#      / \
#     2   3
#    / \
#   4   5
#  /   / \
# 6   7   8
#        /
#       9


def rootToNodePath(root: Node, target, path: list):

    if not root:
        return False

    path.append(root.value)

    left_node = rootToNodePath(root.left, target, path)

    right_node = rootToNodePath(root.right, target, path)

    if not left_node and not right_node and root.value != target:
        path.pop()
    else:
        return True

    if root.value == target:
        return path


path = []
rootToNodePath(tree.root, 9, path)
print(path)

# Here what we do is that while we traverse the tree, we store the path that we take to reach the current node.
# If we reach a node which is not the target, we pop the last element from the path and continue traversing the tree.
# If we reach a node which is the target, we return the path.
# If we reach a leaf node and it is not the target, we return False
# Consider the following example:
# The structure of the tree is:
#       1
#      / \
#     2   3
#    / \
#   4   5
#  /   / \
# 6   7   8
#        /
#       9
# The path to reach the target is: 1->2->5->8->9
# If we reach a leaf node and it is not the target, we return False
# Like lets say we are at 6, which is a leaf node, and it is not the target, we return False and pop 6 from the path and continue traversing the tree.
# We move back to 4, since 6 returned False, we explore 4's right node since it has no right node, it return False and pop 4 from the path and continue traversing the tree.

# The target is 9. Now, let's dry-run the rootToNodePath function step by step:
# Step 1: At Node 1

#     Add 1 to path → [1].
#     Recursively call rootToNodePath for 1.left (Node 2).

# Step 2: At Node 2

#     Add 2 to path → [1, 2].
#     Recursively call rootToNodePath for 2.left (Node 4).

# Step 3: At Node 4

#     Add 4 to path → [1, 2, 4].
#     Recursively call rootToNodePath for 4.left (Node 6).

# Step 4: At Node 6 (Leaf Node)

#     Add 6 to path → [1, 2, 4, 6].
#     Both 6.left and 6.right are None, so recursive calls return False.
#     Since 6 is not the target, perform path.pop() to remove 6.
#         Path after pop → [1, 2, 4].
#     Return False back to Node 4.

# Step 5: Back at Node 4

#     Explore 4.right (which is None), so the call returns False.
#     Since both left and right calls returned False and 4 is not the target, perform path.pop() to remove 4.
#         Path after pop → [1, 2].
#     Return False back to Node 2.

# Step 6: Back at Node 2

#     Now explore 2.right (Node 5).
#     Recursively call rootToNodePath for Node 5.

# Step 7: At Node 5

#     Add 5 to path → [1, 2, 5].
#     Recursively call rootToNodePath for 5.left (Node 7).

# Step 8: At Node 7 (Leaf Node)

#     Add 7 to path → [1, 2, 5, 7].
#     Both 7.left and 7.right are None, so recursive calls return False.
#     Since 7 is not the target, perform path.pop() to remove 7.
#         Path after pop → [1, 2, 5].
#     Return False back to Node 5.

# Step 9: Back at Node 5

#     Now explore 5.right (Node 8).
#     Recursively call rootToNodePath for Node 8.

# Step 10: At Node 8

#     Add 8 to path → [1, 2, 5, 8].
#     Recursively call rootToNodePath for 8.left (Node 9).

# Step 11: At Node 9 (Target Node)

#     Add 9 to path → [1, 2, 5, 8, 9].
#     Since root.value == target, return True.
#     This True propagates back up the call stack to stop further exploration.

# Path Found

# The final path list contains: [1, 2, 5, 8, 9].


# Print all paths from root to leaf
class Solution:
    def __init__(self):
        self.paths = []
        self.path = []

    def Paths(self, root):
        # code here

        def getPaths(root):
            if not root:
                return False

            self.path.append(root.value)

            left_node = getPaths(root.left)

            right_node = getPaths(root.right)

            if (not root.left) and (not root.right):
                self.paths.append(self.path[:])
                self.path.pop()
            else:
                self.path.pop()
                return True

        getPaths(root)
        print(self.paths)
        return self.paths


sol = Solution()

an = sol.Paths(tree.root)

print(an)
