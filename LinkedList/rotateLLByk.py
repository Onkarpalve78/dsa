# LC 61 https://leetcode.com/problems/rotate-list/description/

from SinglyLinkedList import LinkedList, Node

linkedListRotate = LinkedList()

linkedListRotate.append(1)
linkedListRotate.append(2)
linkedListRotate.append(3)
linkedListRotate.append(4)
linkedListRotate.append(5)


def rotateRight(head: Node, k: int):

    if head is None or head.next_node is None or k == 0:
        return head

    current = head
    length = 1

    while current.next_node:
        length += 1
        current = current.next_node

    k = k % length
    if k == 0:
        return head

    current.next_node = head

    steps_to_new_head = length-k

    for _ in range(steps_to_new_head):
        current = current.next_node

    new_node = current.next_node
    current.next_node = None

    return new_node.data


print(rotateRight(linkedListRotate.head, 2))

linkedListRotate.display()
