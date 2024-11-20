# LC 328 https://leetcode.com/problems/odd-even-linked-list/description/

from SinglyLinkedList import LinkedList, Node


oddEvenLL = LinkedList()

oddEvenLL.append(1)
oddEvenLL.append(2)
oddEvenLL.append(3)
oddEvenLL.append(4)
oddEvenLL.append(5)


def oddEvenList(head: Node) -> Node:

    odd = head
    even = head.next_node
    evenStart = even

    while even and even.next_node:
        odd.next_node = even.next_node
        odd = odd.next_node

        even.next_node = odd.next_node
        even = even.next_node

    odd.next_node = evenStart

    return head


oddEvenList(oddEvenLL.head)

oddEvenLL.display()
