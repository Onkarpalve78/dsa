
class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.next_node = None


class LinkedList():
    def __init__(self) -> None:
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node

        else:
            current_node = self.head
            while current_node.next_node is not None:
                # we are looping through the linked list to get the last node and then append the new node to it
                current_node = current_node.next_node
                # this will help us to get the last node by looping through the linked list till we get the last node which has next_node as None

            current_node.next_node = new_node

    def display(self):
        current_node = self.head
        while current_node:
            # we dont need to check for current_node.next_node because we are checking
            # if current_node is None, so it will traverse till the last node and then print None
            print(current_node.data, end=' -> ')
            current_node = current_node.next_node
        print(None)


linkedlist = LinkedList()

linkedlist.append(1)
linkedlist.append(2)
linkedlist.append(3)

linkedlist.display()
