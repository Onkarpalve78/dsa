from SinglyLinkedList import LinkedList, Node

# Using Merge Sort for sorting LL
LL = LinkedList()

LL.append(5)
LL.append(1)
LL.append(3)
LL.append(4)
LL.append(2)


def findMiddle(head):
    slow = head
    fast = head.next_node

    while fast and fast.next_node:
        slow = slow.next_node
        fast = fast.next_node.next_node

    return slow


def mergeTwoLL(LL1: Node, LL2: Node):
    dummyHead = Node(0)
    sorted_list = dummyHead

    while LL1 and LL2:

        if LL1.data > LL2.data:
            sorted_list.next_node = LL2
            # its important to keep moving the node ahead, else it would keep updating same node
            sorted_list = sorted_list.next_node
            LL2 = LL2.next_node

        else:
            sorted_list.next_node = LL1
            sorted_list = sorted_list.next_node
            LL1 = LL1.next_node

    # Appending Remaining node from LL1 and LL2
    sorted_list.next_node = LL1 if LL1 else LL2

    # here returning next_node since we have used Node(0) arbitrarily to start the list
    return dummyHead.next_node


def sortLL(head: Node):
    if not head or not head.next_node:
        return head
    middle = findMiddle(head)
    right = middle.next_node
    middle.next_node = None
    left = head

    leftLL = sortLL(left)
    rightLL = sortLL(right)

    return mergeTwoLL(leftLL, rightLL)


LL.display()

sortedList = sortLL(LL.head)


def displaySortedList(head):
    current_node = head
    while current_node:
        # we dont need to check for current_node.next_node because we are checking
        # if current_node is None, so it will traverse till the last node and then print None
        print(current_node.data, end=' -> ')
        current_node = current_node.next_node
    print(None)


displaySortedList(sortedList)
