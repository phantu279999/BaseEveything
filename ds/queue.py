from typing import Any


class BasicQueue:
    def __init__(self):
        self._queue = []

    def enqueue(self, item: Any) -> bool:
        try:
            self._queue.append(item)
            return True
        except Exception as e:
            print(f"Error during enqueue: {e}")
            return False

    def dequeue(self) -> Any:
        return self._queue.pop(0)

    def qsize(self) -> int:
        return len(self._queue)

    def is_empty(self) -> bool:
        return False if self._queue else True

    def peek(self) -> Any:
        if self.is_empty():
            return "Queue is empty"
        return self._queue[0]

    def clear(self) -> bool:
        try:
            self._queue.clear()
            return True
        except Exception as e:
            print(f"Error during clear: {e}")
            return False

    def __str__(self):
        return "Queue: " + " -> ".join([str(it) for it in self._queue])


if __name__ == '__main__':
    queue = BasicQueue()
    queue.enqueue(1)
    queue.enqueue(3)
    queue.enqueue(7)
    queue.enqueue(11)
    queue.enqueue(14)
    queue.enqueue(16)

    print(queue)