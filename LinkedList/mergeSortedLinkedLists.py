

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def append_node(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node

        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = new_node


def mergeTwoLL(List1: LinkedList, List2: LinkedList):
    mergedList = LinkedList()
    current = mergedList
    list1 = List1.head
    list2 = List2.head

    while list1 and list2:
        print("some")
        if list1.data > list2.data:
            current.next = list2
            current = list2
            list2 = list2.next
        else:
            current.next = list1
            current = list1
            list1 = list1.next

    current = list1 if list1 else list2

    return current.data


linkedList1 = LinkedList()
linkedList2 = LinkedList()

linkedList1.append_node(2)
linkedList1.append_node(4)
linkedList1.append_node(6)

linkedList2.append_node(1)
linkedList2.append_node(3)
linkedList2.append_node(5)

print(mergeTwoLL(linkedList1, linkedList2))
