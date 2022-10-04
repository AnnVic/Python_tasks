class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        if data not in self.items:
            self.items.append(data)

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return self.items == []

    def __len__(self):
        return len(self.items)


stack = Stack()

for i in range(2, 10):
    stack.push(i)
print(stack.pop())
print(len(stack))
