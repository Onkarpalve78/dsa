
class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.next_node = None
        self.prev_node = None


class DoublyLinkedList():
    def __init__(self) -> None:
        self.head = None

    def isEmpty(self):
        return self.head is None

    def append(self, data):
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
            print(current_node.data, end='<->')
            current_node = current_node.next_node
        print(None)

    def displayBackwards(self):
        current_node = self.head

        while current_node and current_node.next_node is not None:
            current_node = current_node.next_node

        while current_node:
            print(current_node.data, end='<->')
            current_node = current_node.prev_node
        print(None)
        # lesson learnt dont nest while loops while also updating the same thing on which both loops are dependent upon it casuses infinite loops


doublyLinkedList = DoublyLinkedList()
doublyLinkedList.append(1)
doublyLinkedList.append(2)
doublyLinkedList.append(3)
doublyLinkedList.append(4)

doublyLinkedList.displayForwards()
doublyLinkedList.displayBackwards()
