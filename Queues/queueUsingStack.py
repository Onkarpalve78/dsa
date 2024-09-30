

class Stacked_Queue():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int):
        self.stack1.append(x)

    def pop(self):

        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    def peek(self):

        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1]

    def empty(self):

        return len(self.stack1) == 0 and len(self.stack2) == 0


stackedQueue = Stacked_Queue()

stackedQueue.push(1)
stackedQueue.push(2)
stackedQueue.push(3)
stackedQueue.push(4)
stackedQueue.push(5)
stackedQueue.push(6)

print(stackedQueue.peek())
