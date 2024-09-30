from collections import deque


class QueuedStack():
    def __init__(self) -> None:
        self.queue = deque()

    def push(self, val: int):
        self.queue.append(val)

    def pop(self):

        for i in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())

        return self.queue.popleft()

    def top(self):
        return self.queue[-1]

    def empty(self):
        return len(self.queue) == 0
