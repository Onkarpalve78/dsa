class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def partitionList(root: Node, x: int) -> Node:
    # Create two dummy nodes for two partitions
    less_head = Node(0)
    greater_equal_head = Node(0)

    # Pointers for the two partitions
    less = less_head
    greater_equal = greater_equal_head

    # Traverse the original list
    current = root
    while current:
        if current.val < x:
            less.next = current
            less = less.next
        else:
            greater_equal.next = current
            greater_equal = greater_equal.next
        current = current.next

    # Connect the two partitions
    less.next = greater_equal_head.next
    greater_equal.next = None

    return less_head.next

# Helper function to create a linked list from a list of values


def createLinkedList(values):
    dummy = Node(0)
    current = dummy
    for val in values:
        current.next = Node(val)
        current = current.next
    return dummy.next

# Helper function to convert linked list to list for printing


def linkedListToList(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


# Example usage
if __name__ == "__main__":
    # Create a sample linked list: 1 -> 4 -> 3 -> 2 -> 5 -> 2
    values = [1, 4, 3, 2, 5, 2]
    head = createLinkedList(values)

    # Partition the list with x = 3
    partitioned = partitionList(head, 4)

    # Print the result
    print(linkedListToList(partitioned))
