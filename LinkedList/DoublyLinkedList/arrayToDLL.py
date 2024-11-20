from DoublyLinkedList import DoublyLinkedList, Node


class DLLArr(DoublyLinkedList):
    def __init__(self):
        super().__init__()

    def arrToDLL(self, nums: list[int]) -> Node:
        self.head = Node(nums[0])
        current_node = self.head
        for i in range(1, len(nums)):
            new_node = Node(nums[i])
            current_node.next = new_node
            new_node.prev = current_node
            current_node = new_node

        return self.head

    def displayLL(self):
        current_node = self.head
        while current_node:
            print(current_node.val, end="<=>")
            current_node = current_node.next

        print(None)

    def deleteHeadOfDLL(self):
        current_node = self.head
        self.head = current_node.next
        current_node.next = None

    def deleteTailOfDLL(self):
        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next
        prev = current_node.prev
        prev.next = None
        current_node.prev = None

    def deleteKthNode(self, k):
        current_node = self.head

        count = 1
        while current_node.next is not None and count != k:
            print(current_node.val)
            count += 1
            current_node = current_node.next

        # if DLL has single node
        if current_node.next is None and current_node.prev is None:
            self.head = None

        # if Kth node is the last node
        elif current_node.next is None:
            self.deleteTailOfDLL()

        # if Kth node is head node
        elif current_node.prev is None:
            self.deleteHeadOfDLL()

        # for any intermediate nodes
        else:
            prev = current_node.prev
            next = current_node.next

            prev.next = next
            next.prev = prev

            current_node.next = None
            current_node.prev = None

    def reverseDLL(self):
        current_node = self.head
        prev = None
        while current_node:
            prev = current_node.prev
            current_node.prev = current_node.next
            current_node.next = prev

            # since we're making curr.next=curr.prev we need to move backwards in order to move to next elements
            current_node = current_node.prev
        # At this point prev node is at the 2nd last node, doing prev.prev points it to the last node of the original LL
        self.head = prev.prev


arrDLL = DLLArr()
arrDLL.arrToDLL([1, 2, 3, 4, 5, 6, 7, 8, 69])
arrDLL.displayBackwards()
arrDLL.displayLL()

arrDLL.deleteKthNode(5)
arrDLL.displayLL()
arrDLL.reverseDLL()
arrDLL.displayLL()
