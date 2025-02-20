from typing import Any
from ds.queue import BasicQueue


class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data: Any) -> None:
        if self.data is None:
            self.data = data
        else:
            q = BasicQueue()
            q.enqueue(self)
            while not q.is_empty():
                item = q.dequeue()
                if item.left is None:
                    item.left = TreeNode(data)
                    break
                if item.right is None:
                    item.right = TreeNode(data)
                    break
                q.enqueue(item.left)
                q.enqueue(item.right)

    def preorder_traversal(self, root):
        if root:
            print(root.data)
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)


if __name__ == '__main__':
    root = TreeNode(15)
    root.insert(7)
    root.insert(6)
    root.insert(18)
    root.insert(19)
    root.insert(1)
    root.insert(5)
    root.insert(23)

    root.preorder_traversal(root)