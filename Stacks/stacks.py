
class Stack():
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return len(self.items)==0
    
    def push(self,item):
        return self.items.append(item)
    
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            raise IndexError('Pop from an empty stack')
    
    def peek(self):
        if not self.isEmpty():
            return print(self.items[-1])
        else:
            raise IndexError("Peek from an empty stack")
    
stack=Stack()

stack.push(1)
stack.push(2)
stack.push(10)
print(stack.items)
stack.peek()

stack.pop()
print(stack.items)