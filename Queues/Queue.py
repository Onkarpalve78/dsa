
class Queue():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        return self.items.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        else:
            return IndexError('Pop from an empty queue')

    def front(self):
        if not self.isEmpty():
            return self.items[0]
        else:
            return IndexError('Empty queue')

    def size(self):
        return len(self.items)


queue = Queue()
queue.enqueue(8)
queue.enqueue(9)
queue.enqueue(6)
print(queue.items)
print('Size', queue.size())
queue.dequeue()
print(queue.items)

# referencing concept
a = [1, 2, 3]
b = a
b.append(4)
print(a)
