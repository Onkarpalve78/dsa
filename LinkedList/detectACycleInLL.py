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

testLLwithNoCycle = LinkedList()
testLLwithNoCycle.append(11)
testLLwithNoCycle.append(11)
testLLwithNoCycle.append(11)


# TC O(N) SC O(N)
def detectCycle(LList: LinkedList) -> bool:

    if LList.head is None or LList.head.next_node is None:
        return False  # Cant have cycle in empty or len 1 LL

    current_node = LList.head
    node_hash = set()
    while current_node:
        if current_node in node_hash:
            return True
        else:
            node_hash.add(current_node)
            current_node = current_node.next_node
    return False


def detectCycleOptimal(LList: LinkedList) -> bool:
    if LList.head is None or LList.head.next_node is None:
        return False  # Cant have cycle in empty or len 1 LL

    slow, fast = LList.head, LList.head

    while fast.next_node is not None or fast.next_node.next_node is not None:
        slow = slow.next_node
        fast = fast.next_node.next_node

        if slow == fast:
            return True

    return False


print(detectCycle(testLLwithNoCycle))
print(detectCycleOptimal(linkedList))
