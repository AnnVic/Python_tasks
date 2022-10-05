from typing import Generic, TypeVar
T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self):
        self.items = []

    def push(self, data: T) -> None:
        if data not in self.items:
            self.items.append(data)

    def pop(self) -> T:
        if self.items:
            return self.items.pop()

    def is_empty(self) -> bool:
        return self.items == []

    def __len__(self) -> int:
        return len(self.items)


stack = Stack()

for i in range(2, 10):
    stack.push(i)
print(stack.pop())
print(len(stack))
