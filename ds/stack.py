from typing import Any


class Stack:
    def __init__(self):
        self.__items = []


    def push(self, item: Any) -> None:
        self.__items.append(item)

    def pop(self) -> Any:
        return self.__items.pop()

    def peek(self) -> Any:
        return self.__items[len(self.__items) - 1]

    def size(self) -> int:
        return len(self.__items)

    def is_empty(self) -> bool:
        return not self.__items

    def display(self) -> None:
        print(self.__items)


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(4)
    stack.push(6)
    stack.push(8)
    stack.push(22)
    stack.push(44)

    stack.display()

    stack.pop()

    stack.display()