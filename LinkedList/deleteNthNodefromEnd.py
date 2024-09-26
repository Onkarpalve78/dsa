# LC 19 https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
from SinglyLinkedList import LinkedList

CurrLList = LinkedList()

CurrLList.append(1)
CurrLList.append(2)
CurrLList.append(3)
CurrLList.append(4)
CurrLList.append(5)

N = int(input("Enter N: "))


def deleteNthNodeFromEnd(LList: LinkedList):
    slow = LList.head
    fast = LList.head

    for _ in range(N):
        fast = fast.next_node

    if fast is None:
        return LList.head.next_node

    while fast.next_node is not None:
        fast = fast.next_node
        slow = slow.next_node

    slow.next_node = slow.next_node.next_node

    return LList.head


CurrLList.display()

deleteNthNodeFromEnd(CurrLList)

CurrLList.display()
