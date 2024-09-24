

class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.next_node = None


class StackLinkedList():
    def __init__(self) -> None:
        self.head = None

    def isEmpty(self):
        return self.head is None

    def push(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.head = newNode
        else:
            current_node = self.head
            while current_node.next_node is not None:
                current_node = current_node.next_node
            current_node.next_node = newNode

    def pop(self):
        current_node = self.head
        prev_node = None
        if current_node is None:
            return IndexError('List is empty')
        else:
            while current_node.next_node is not None:
                prev_node = current_node
                print(f"prevNode {prev_node.data}")
                current_node = current_node.next_node
                print(f"currentNode {current_node.data}")

            if prev_node is not None:
                prev_node.next_node = None
            else:
                self.head = None

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' -> ')
            current_node = current_node.next_node

        print(None)


stackLinkedList = StackLinkedList()

stackLinkedList.push(1)
stackLinkedList.push(2)
stackLinkedList.push(3)
stackLinkedList.display()
stackLinkedList.pop()

stackLinkedList.display()
