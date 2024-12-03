# LC 111 https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
from BinaryTree import Node, BinaryTree
from collections import deque

tree = BinaryTree(1)

tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.right.left = Node(69)
tree.root.right.right = Node(69)

tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

tree.root.left.left.left = Node(6)
tree.root.left.right.left = Node(7)


def minDepth(root: Node):

    if not root:
        return 0

    bfs = []
    queue = deque()
    queue.append(root)

    ans = float('inf')
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
            if not node.left and not node.right:
                if len(bfs) < ans:
                    ans = len(bfs)
        bfs.append(level)
    return ans+1


print(minDepth(tree.root))
