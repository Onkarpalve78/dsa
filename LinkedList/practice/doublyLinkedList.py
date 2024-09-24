

class Node():
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.prev_node = None


class DoublyLinkedList():
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def insert_node(self, data):
        new_node = Node(data)

        if self.isEmpty():
            self.head = new_node

        else:
            current_node = self.head
            while current_node.next_node is not None:
                current_node = current_node.next_node
            current_node.next_node = new_node
            new_node.prev_node = current_node

    def displayForwards(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end="<=>")
            current_node = current_node.next_node
        print(None)

    def displayBackwards(self):
        current_node = self.head

        while current_node and current_node.next_node is not None:
            current_node = current_node.next_node

        while current_node:
            print(current_node.data, end="<=>")
            current_node = current_node.prev_node
        print(None)


doublyLinkedList = DoublyLinkedList()

doublyLinkedList.insert_node(1)
doublyLinkedList.insert_node(2)
doublyLinkedList.insert_node(3)
doublyLinkedList.insert_node(4)

doublyLinkedList.displayForwards()
doublyLinkedList.displayBackwards()
