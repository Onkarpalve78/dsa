# LC 237 https://leetcode.com/problems/delete-node-in-a-linked-list/description/

from SinglyLinkedList import LinkedList, Node

LL = LinkedList()
LL.append(1)
LL.append(2)
thirdNode = LL.append(3)
LL.append(4)
LL.display()


def deleteNode(node: Node):
    node.data = node.next_node.data
    node.next_node = node.next_node.next_node
    return node


deleteNode(Node(3))

LL.display()
