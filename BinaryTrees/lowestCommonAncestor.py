from BinaryTree import BinaryTree, Node
tree2 = BinaryTree(1)

tree2.root.left = Node(2)
tree2.root.right = Node(3)

tree2.root.left.left = Node(4)
tree2.root.left.right = Node(5)

tree2.root.left.left.left = Node(6)
tree2.root.left.right.left = Node(7)
tree2.root.left.right.right = Node(8)
tree2.root.left.right.right.left = Node(9)

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


def lowestCommonAncestor(root: Node, p: Node, q: Node) -> Node:
    if not root or root.value == p.value or root.value == q.value:
        return root

    left_node = lowestCommonAncestor(root.left, p, q)
    right_node = lowestCommonAncestor(root.right, p, q)

    if left_node is None:
        return right_node

    if right_node is None:
        return left_node

    else:
        return root.value


print(lowestCommonAncestor(tree2.root, Node(6), Node(9)))


# The goal of the code is to find the Lowest Common Ancestor (LCA) of two nodes p and q in a binary tree. The LCA of two nodes is the lowest (deepest) node in the tree that has both nodes as descendants (including the node itself).

# In this case:

#     We are given a binary tree with structure:

#            1
#           / \
#          2   3
#         / \
#        4   5
#       /   / \
#      6   7   8
#             /
#            9

#     We need to find the LCA of nodes 6 and 9.

# Code Explanation
# Base Case

# if not root or root.value == p.value or root.value == q.value:
#     return root

#     If root is None (we have reached a null node), return None.
#     If the current node matches either p or q, return the current node.

# Recursive Case

# left_node = lowestCommonAncestor(root.left, p, q)
# right_node = lowestCommonAncestor(root.right, p, q)

#     Recur on the left and right subtrees:
#         left_node stores the LCA (or matched node) from the left subtree.
#         right_node stores the LCA (or matched node) from the right subtree.

# Decision Logic

# if left_node is None:
#     return right_node

# if right_node is None:
#     return left_node
# else:
#     return root.value

#     If one side returns None, it means both nodes are in the opposite subtree. So return the non-None node.
#     If both left_node and right_node are non-None, the current node is the LCA, and we return root.value.

# Dry Run Step-by-Step

# We are calling lowestCommonAncestor(tree2.root, Node(6), Node(9)).

# The tree structure is:

#          1
#         / \
#        2   3
#       / \
#      4   5
#     /   / \
#    6   7   8
#           /
#          9

# We need to find the LCA of 6 and 9.
# Step 1: Start at Node 1

#     Current Node: 1
#     Recur on root.left (Node 2).
#     Recur on root.right (Node 3).

# Step 2: Traverse Left Subtree (Node 2)

#     Current Node: 2
#     Recur on root.left (Node 4).
#     Recur on root.right (Node 5).

# Step 3: Traverse Left Subtree of Node 2 (Node 4)

#     Current Node: 4
#     Recur on root.left (Node 6).
#     Recur on root.right (None).

# Node 6 (Base Case)

#     Current Node: 6
#     root.value == p.value, so return Node(6).

# Back at Node 4

#     left_node = Node(6)
#     right_node = None.
#     Since right_node is None, return left_node → Node(6).

# Step 4: Traverse Right Subtree of Node 2 (Node 5)

#     Current Node: 5
#     Recur on root.left (Node 7).
#     Recur on root.right (Node 8).

# Node 7 (Leaf Node)

#     Current Node: 7
#     Both left and right are None, return None.

# Node 8

#     Current Node: 8
#     Recur on root.left (Node 9).
#     Recur on root.right (None).

# Node 9 (Base Case)

#     Current Node: 9
#     root.value == q.value, so return Node(9).

# Back at Node 8

#     left_node = Node(9)
#     right_node = None.
#     Since right_node is None, return left_node → Node(9).

# Back at Node 5

#     left_node = None
#     right_node = Node(9)
#     Since left_node is None, return right_node → Node(9).

# Back at Node 2

#     left_node = Node(6)
#     right_node = Node(9)

# Both left_node and right_node are non-None, so:

#     Node 2 is the LCA of Nodes 6 and 9.
#     Return Node(2).

# Step 5: Traverse Right Subtree of Node 1 (Node 3)

#     Current Node: 3

#     Recur on root.left and root.right (both are None).

#     Both calls return None, so return None.

# Back at Node 1

#     left_node = Node(2) (LCA found in left subtree).
#     right_node = None.

# Since right_node is None, return left_node → Node(2).
# Final Result

# The Lowest Common Ancestor (LCA) of Nodes 6 and 9 is Node 2.
# Output

# 2

# Key Observations

#     We recursively explore both left and right subtrees.
#     If we find one node in one subtree and another node in the other subtree, the current node is the LCA.
#     If one subtree is None, the other subtree contains the LCA.
