from SinglyLinkedList import LinkedList, Node

linkedlist1 = LinkedList()
linkedlist2 = LinkedList()

linkedlist1.append(1)
linkedlist1.append(5)
interSectNode: Node = linkedlist1.append(4)
linkedlist1.append(3)
linkedlist1.append(2)

linkedlist2.append(7)
linkedlist2.head.next_node = interSectNode
linkedlist2.append(8)
linkedlist2.append(9)


linkedlist1.display()
linkedlist2.display()


def intersectionPresent(L1: LinkedList, L2: LinkedList):
    d1 = L1.head
    d2 = L2.head

    while d1 != d2:

        d1 = L2.head if d1 is None else d1.next_node
        d2 = L1.head if d2 is None else d2.next_node

    return d1.data  # either return d1 or d2 both would be the same node where intersection has happened


print(intersectionPresent(linkedlist1, linkedlist2))
