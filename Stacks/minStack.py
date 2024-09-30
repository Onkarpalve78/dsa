# LC 155 https://leetcode.com/problems/min-stack/description/


class MinStack():
    def __init__(self):
        self.stack = []
        self.minStack = []

    def isEmpty(self):
        return self.stack == 0

    def push(self, data):
        self.stack.append(data)
        minValue = min(data, self.minStack[-1] if self.minStack else data)
        self.minStack.append(minValue)

    def pop(self):
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minStack[-1]


minStack = MinStack()

minStack.push(1)
minStack.push(-1)
minStack.push(3)
minStack.push(0)
minStack.push(6)

print(minStack.getMin())
