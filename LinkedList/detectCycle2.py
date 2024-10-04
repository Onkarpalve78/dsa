# LC 142 https://leetcode.com/problems/linked-list-cycle-ii/description/

from SinglyLinkedList import LinkedList, Node

linkedList = LinkedList()

linkedList.append(1)
cycleAtNode: Node = linkedList.append(2)
linkedList.append(3)
linkedList.append(4)

current_node: Node = linkedList.head
while current_node:
    current_node = current_node.next_node
    if current_node.next_node is None:
        current_node.next_node = cycleAtNode
        break


def findCycleNode(LList: LinkedList):
    slow: Node = LList.head
    fast: Node = LList.head
    entry: Node = LList.head

    while fast and fast.next_node:
        slow = slow.next_node
        fast = fast.next_node.next_node
        if slow == fast:
            while slow != entry:
                slow = slow.next_node
                entry = entry.next_node
            return entry.data

    return None


print(findCycleNode(linkedList))


def findCycleNodeMyCode(LList: LinkedList):
    slow: Node = LList.head
    fast: Node = LList.head
    entry: Node = LList.head
    isCycle = False
    while fast and fast.next_node:
        slow = slow.next_node
        fast = fast.next_node.next_node
        if slow == fast:
            isCycle = True
            break

    while slow != entry and isCycle:
        slow = slow.next_node
        entry = entry.next_node
        return entry.data

    return None


print(findCycleNodeMyCode(linkedList))
