

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

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end="=>")
            current_node = current_node.next

        print(None)

    def displayMiddleNode(self):
        slow, fast = self.head, self.head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        print(slow.data)
        return slow


linkedList = LinkedList()

linkedList.append_node(10)
linkedList.append_node(11)
linkedList.append_node(12)
linkedList.append_node(13)
linkedList.append_node(14)
linkedList.append_node(15)


linkedList.display()

linkedList.displayMiddleNode()
