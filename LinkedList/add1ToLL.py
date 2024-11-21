# https://www.geeksforgeeks.org/problems/add-1-to-a-number-represented-as-linked-list/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=add-1-to-a-number-represented-as-linked-list
from SinglyLinkedList import LinkedList, Node

linkedList = LinkedList()

linkedList.append(1)
linkedList.append(3)
linkedList.append(2)
linkedList.append(4)
linkedList.append(3)
linkedList.append(9)


def addOneToLL(head: Node):

    # Reverse given LL
    def reverseHead(head):
        current_node = head
        prev_node = None
        while current_node:
            temp_next_node = current_node.next_node
            current_node.next_node = prev_node
            prev_node = current_node
            current_node = temp_next_node
        return prev_node
    if head.next_node:
        head = reverseHead(head)

    carry = 0
    sum = 0

    ans_node = Node(0)
    temp = ans_node
    current_node = head
    carry = 1  # starting carry with 1 cuz we need to add 1 in the summation
    while current_node or carry:
        sum = 0
        if current_node:
            sum = current_node.data
            current_node = current_node.next_node

        sum += carry

        carry = sum//10

        new_node = Node(sum % 10)

        ans_node.next_node = new_node
        ans_node = ans_node.next_node

    head = reverseHead(temp.next_node)

    return head


ll = addOneToLL(linkedList.head)

while ll:
    print(ll.data, end="->")
    ll = ll.next_node

print(None)


def addOneToLLRecursive(head: Node):
    if not head:
        return head

    def addOne(node: Node):
        if node is None:
            return 1
        r_carry = addOne(node.next_node)
        sum = 0
        sum = node.data+r_carry
        node.data = sum % 10  # directly updating the node data

        carry = sum//10
        return carry

    carry = addOne(head)

    # If carry exists create a new node and make that the head
    if carry:
        new_head = Node(carry)
        new_head.next_node = head
        head = new_head

    return head


linkedList2 = LinkedList()


linkedList2.append(5)
linkedList2.append(4)
linkedList2.append(8)
linkedList2.append(9)


ll2 = addOneToLLRecursive(linkedList2.head)

while ll2:
    print(ll2.data, end="->")
    ll2 = ll2.next_node
