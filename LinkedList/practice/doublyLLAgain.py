

class Node():
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoublyLL():
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def append_node(self, val):
        new_node = Node(val)
        if self.isEmpty():
            self.head = new_node

        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = new_node
            new_node.prev = current_node

    def displayBackwards(self):
        current_node = self.head

        while current_node and current_node.next is not None:
            current_node = current_node.next

        while current_node:
            print(current_node.val, end="<=>")
            current_node = current_node.prev

        print(None)


dll = DoublyLL()
dll.append_node(1)
dll.append_node(2)
dll.append_node(3)
dll.append_node(4)

dll.displayBackwards()
