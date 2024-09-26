from SinglyLinkedList import LinkedList, Node

linkedList = LinkedList()

linkedList.append(1)
linkedList.append(2)
linkedList.append(3)
linkedList.append(2)
linkedList.append(12)


def isPalindrome(LList: LinkedList) -> bool:
    slow, fast = LList.head, LList.head

    while fast and fast.next_node:
        slow = slow.next_node
        fast = fast.next_node

    prev = None
    while slow:
        temp = slow.next_node
        slow.next_node = prev
        prev = slow
        slow = temp

    left, right = LList.head, prev
    while right:
        if left.data != right.data:
            return False
        left = left.next_node
        right = right.next_node

    return True


print(isPalindrome(linkedList))
