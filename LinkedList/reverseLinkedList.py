

class Node():
    def __init__(self, data):
        self.data = data
        self.next_node = None


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
            while current_node.next_node is not None:
                current_node = current_node.next_node

            current_node.next_node = new_node

    def printList(self):
        current_node = self.head

        while current_node:
            print(current_node.data, end="=>")
            current_node = current_node.next_node

        print(None)

    def reverseList(self):
        current_node = self.head
        previos_node = None
        while current_node:
            temp_next_node = current_node.next_node
            # Keeping next_node's data so as to not lose the data of the rest of the further
            # linkedlist after we point our next_node to the previous node
            current_node.next_node = previos_node
            previos_node = current_node
            current_node = temp_next_node
        self.head = previos_node


linkedList = LinkedList()

linkedList.append_node(1)
linkedList.append_node(2)
linkedList.append_node(3)
linkedList.append_node(4)

linkedList.printList()

linkedList.reverseList()

linkedList.printList()
