"""Creating stacks using classes
Stack work in LIFO which is Last in First Out"""


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()

    def isEmpty(self):
        return len(self.stack) == 0


mystack = Stack()
mystack.push(10)
mystack.push(50)
mystack.push(100)
mystack.push(70)
print(mystack.pop())
print(mystack.stack)
