from typing import Any


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SimpleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data: Any) -> None:
        if self.head is None:
            self.head = Node(data)
        _temp = self.head
        while _temp.next:
            _temp = _temp.next
        _temp.next = Node(data)

    def insert(self, index: int, data: Any) -> None:
        if self.size() < index:
            raise Exception("Index out of range")
        if index == -1:
            # Case add last linkedlist
            self.append(data)
        elif index == 0:
            # Case add first linkedlist
            node = Node(data)
            node.next = self.head
            self.head = node
        else:
            _temp = self.head
            for _ in range(index - 1):
                _temp = _temp.next
            node = Node(data)
            temp_next = _temp.next
            _temp.next = node
            node.next = temp_next

    def delete(self, index: int) -> None:
        if self.size() < index:
            raise Exception("Index out of range")

        if index == 0:
            self.head = self.head.next
        elif index == -1:
            _temp = self.head
            while _temp.next:
                _temp = _temp.next
            _temp.next = None
        else:
            _temp = self.head
            for _ in range(index - 1):
                _temp = _temp.next
            _temp.next = _temp.next.next


    def size(self) -> int:
        _temp = self.head
        count = 0
        while _temp:
            count += 1
            _temp = _temp.next
        return count

    def traverse(self):
        _temp = self.head
        nodes = []
        while _temp.next:
            nodes.append(str(_temp.data))
            _temp = _temp.next
        print(" -> ".join(nodes))


if __name__ == "__main__":
    ll = SimpleLinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(6)
    ll.append(11)
    ll.insert(4, 77)
    ll.append(14)
    ll.traverse()
    # 1 -> 1 -> 3 -> 6 -> 77 -> 11
    ll.delete(5)
    ll.delete(3)
    ll.traverse()
    # 1 -> 1 -> 3 -> 77
