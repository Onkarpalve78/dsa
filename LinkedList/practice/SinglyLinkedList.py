

class Node():
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList():
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

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end="=>")
            current_node = current_node.next_node
        print(None)


linked_list = LinkedList()

linked_list.insert_node(1)
linked_list.insert_node(2)
linked_list.insert_node(3)

linked_list.display()
