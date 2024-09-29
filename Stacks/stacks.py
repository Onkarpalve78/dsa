
class Stack():
    def __init__(self):
        self.top = -1
        self.max_size = 100
        self.items = [0]*self.max_size

    def isEmpty(self):
        return self.top == -1

    def push(self, item):
        self.top += 1
        if self.top < self.max_size:
            self.items[self.top] = item
        else:
            raise IndexError("Max stack size reached!")

    def pop(self):
        if not self.isEmpty():
            x = self.items[self.top]
            self.top -= 1
            return x
        else:
            raise IndexError('Pop from an empty stack')

    def peek(self):
        if not self.isEmpty():
            return self.items[self.top]
        else:
            raise IndexError("Peek from an empty stack")

    def size(self):
        return self.top+1


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)


stack.peek()

stack.pop()
stack.pop()

stack.push(6)
stack.push(7)
print(stack.items)


stack.peek()
print("size: ", stack.size())
