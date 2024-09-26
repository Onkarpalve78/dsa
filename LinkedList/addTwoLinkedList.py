# LC 2 https://leetcode.com/problems/add-two-numbers/description/

from SinglyLinkedList import LinkedList, Node


L1 = LinkedList()
L2 = LinkedList()

L1.append(2)
L1.append(4)
L1.append(3)

L2.append(5)
L2.append(6)
L2.append(7)
L2.append(9)


def addTwoLists(L1: LinkedList, L2: LinkedList):
    ans_node: Node = Node(0)
    temp: Node = ans_node
    carry = 0
    l1 = L1.head
    l2 = L2.head

    while (l1 or l2) or carry:
        sum = 0
        if l1:
            sum += l1.data
            l1 = l1.next_node

        if l2:
            sum += l2.data
            l2 = l2.next_node

        sum += carry
        carry = sum//10

        new_node = Node(sum % 10)
        # to add the unit value of the sum in the ans_node
        temp.next_node = new_node
        temp = temp.next_node

    return ans_node.next_node


print(addTwoLists(L1, L2))
