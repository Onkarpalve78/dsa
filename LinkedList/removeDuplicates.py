# LC 83 https://leetcode.com/problems/remove-duplicates-from-sorted-list/

from SinglyLinkedList import LinkedList, Node

L1 = LinkedList()

L1.append(1)
L1.append(1)
L1.append(2)
L1.append(2)
L1.append(3)
L1.append(3)

L1.display()


def removeDuplicates(head: Node) -> Node:
    current_node = head
    new_node = current_node
    new_head = new_node

    while current_node:
        current_node = current_node.next_node
        if current_node is None:
            new_node.next_node = None
            break
        elif current_node.data == new_node.data:
            continue
        elif current_node.data != new_node.data:
            new_node.next_node = current_node
            new_node = new_node.next_node
    return new_head


L1.head = removeDuplicates(L1.head)

L1.display()
