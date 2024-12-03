# LC 203 https://leetcode.com/problems/remove-linked-list-elements/description/

from SinglyLinkedList import LinkedList, Node


L1 = LinkedList()


L1.append(1)
L1.append(2)
L1.append(2)
L1.append(2)
L1.append(2)
L1.append(2)
L1.append(2)
L1.append(4)
L1.append(3)
L1.append(2)
L1.append(4)
L1.append(3)


def deleteNodesOfN(head: Node, N: int):
    if head.data == N:
        while head and head.data == N:
            head = head.next_node
    ans = Node(0)
    ans.next_node = head
    current = ans

    while current:
        while current.next_node and current.next_node.data == N:
            current.next_node = current.next_node.next_node
        current = current.next_node
    return ans.next_node


newLL = deleteNodesOfN(L1.head, 2)

while newLL:
    print(newLL.data, end="->")
    newLL = newLL.next_node

# L1.display()
