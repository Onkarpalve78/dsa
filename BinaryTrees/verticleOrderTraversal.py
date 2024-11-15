from BinaryTree import BinaryTree, Node
from collections import deque, defaultdict

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


def verticelOrderTraversal(root):
    if not root:
        return []

    nodes = defaultdict(lambda: defaultdict(list))

    queue = deque()
    queue.append((root, 0, 0))

    while queue:
        node, verticle_level, level = queue.popleft()

        nodes[verticle_level][level].append(node.value)

        if node.left:
            queue.append((node.left, verticle_level-1, level+1))

        if node.right:
            queue.append((node.right, verticle_level+1, level+1))

    ans = []

    for kev, y_val in sorted(nodes.items()):
        # this is to sort verticle levels from -2,-1,0,1,2
        col = []
        for x_key, x_val in sorted(y_val.items()):
            # this is to sort the horizontal levels 0,1,2,3
            col.extend(sorted(x_val))
            # this is to sort the values in the horizontal levels

        ans.append(col)

    return ans


print(verticelOrderTraversal(tree.root))
