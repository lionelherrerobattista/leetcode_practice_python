class MinStack:
    def __init__(self):
        self.stack = []
        self.min_element = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_element:
            self.min_element.append(min(self.min_element[-1], val))
        else:
            self.min_element.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_element.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_element[-1]


minStack = MinStack()
minStack.push(1)
minStack.push(2)
minStack.push(0)
minStack.getMin()
minStack.pop()
minStack.top()
minStack.getMin()
