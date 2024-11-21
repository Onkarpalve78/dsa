# https://www.geeksforgeeks.org/problems/delete-all-occurrences-of-a-given-key-in-a-doubly-linked-list/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=delete-all-occurrences-of-a-given-key-in-a-doubly-linked-list

from arrayToDLL import DLLArr, Node

arrDLL = DLLArr()
arrDLL.arrToDLL([4, 1, 2, 3, 4, 5, 4, 7, 8, 4, 9, 4])


arrDLL.displayLL()


def deleteAllKNodes(head: Node, k: int):
    if not head:
        return head

    current_node = head

    while current_node:

        next = current_node.next
        prev = current_node.prev

        if current_node.val == k:
            if not current_node.prev:
                next.prev = None
                head = next
                print(current_node.val, head.val, head.prev, head.next.val)

            elif not current_node.next:
                prev.next = None
            else:
                prev.next = next
                next.prev = prev

            # No need to do this to delete them, this just causes mayhem
            # current_node.prev = None
            # current_node.next = None

        current_node = current_node.next

    return head


deleteAllKNodes(arrDLL.head, k=4)

# The 4 at the start of LL still shows up cuz the og LL still has it as head
arrDLL.displayLL()
