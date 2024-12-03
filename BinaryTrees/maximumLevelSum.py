# LC 1161 https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/

from BinaryTree import Node, BinaryTree
from collections import deque

tree = BinaryTree(1)

tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.right.left = Node(69)
tree.root.right.right = Node(-80)

tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

tree.root.left.left.left = Node(6)
tree.root.left.right.left = Node(7)

# Binary Tree Structure:
#           1
#         /   \
#        2     3
#       / \   / \
#      4   5 69 69
#     /   /
#    6   7


def maxLevelSum(root) -> int:
    if not root:
        return root

    bfs = []

    queue = deque()
    queue.append(root)

    total_sum = float('-inf')
    ans = None
    while queue:
        level = []
        size = len(queue)
        level_sum = 0

        for _ in range(size):
            node: Node = queue.popleft()
            level.append(node.value)
            level_sum += node.value

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if level_sum > total_sum:
            ans = len(bfs)+1
            total_sum = level_sum

        bfs.append(level)

    return ans, bfs


print(maxLevelSum(tree.root))
