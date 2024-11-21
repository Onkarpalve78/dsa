# https://www.geeksforgeeks.org/problems/find-length-of-loop/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=find-length-of-loop

from SinglyLinkedList import LinkedList, Node

linkedList = LinkedList()

linkedList.append(1)
linkedList.append(3)
cycleAtNode: Node = linkedList.append(2)
linkedList.append(4)
linkedList.append(3)
linkedList.append(4)

current_node: Node = linkedList.head
while current_node:
    current_node = current_node.next_node
    if current_node.next_node is None:
        current_node.next_node = cycleAtNode
        break


def lengthOfCycle(head: Node) -> int:

    start_node = head
    slow, fast = head, head

    # keeping fast and fast.next.next instead of just [while fast:] is imp here, cuz what happens if you're at 2nd last node
    while fast and fast.next_node:
        slow = slow.next_node
        fast = fast.next_node.next_node
        if slow == fast:
            break

    # Condition when there is no cycle in the LL
    if not fast or not fast.next:
        return 0

    cycleStartNode = None
    while slow:
        slow = slow.next_node
        start_node = start_node.next_node
        if slow == start_node:
            cycleStartNode = slow
            break

    slow = slow.next_node
    count = 0
    while slow:
        count += 1
        slow = slow.next_node
        if slow == cycleStartNode:
            break

    return count+1 if count else count


print(lengthOfCycle(linkedList.head))
