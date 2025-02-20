from typing import Any
from ds.queue import BasicQueue

class BinaryTree:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def __iter__(self):
        return iter(self.level_order_with_queue())

    def insert(self, data: Any) -> None:
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = BinaryTree(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = BinaryTree(data)
                else:
                    self.right.insert(data)

    def search(self, data: Any) -> bool:
        if self.data is None:
            return False

        if self.data == data:
            return True
        if data < self.data and self.left is not None:
            return self.left.search(data)
        elif self.right is not None:
            return self.right.search(data)
        return False

    def height(self) -> int:
        def _helper(root):
            if root is None:
                return 0
            l = _helper(root.left)
            r = _helper(root.right)
            return max(l, r) + 1
        return _helper(self)

    def level_order_traversal(self) -> list[Any]:
        def _helper(root, level):
            res = []
            if root is None:
                return res
            if level == 0:
                res.append(root.data)
            else:
                res += _helper(root.left, level - 1)
                res += _helper(root.right, level - 1)
            return res

        res = []
        height = self.height()
        for level in range(height):
            res.append(_helper(self, level))
        return res

    def level_order_with_queue(self) -> list[Any]:
        queue = BasicQueue()
        queue.enqueue(self)
        level_nodes = []
        while not queue.is_empty():
            node = queue.dequeue()
            level_nodes.append(node.data)
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return level_nodes

    def preorder(self) -> None:
        print(self.data, end=" ")
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()

    def inorder(self) -> None:
        if self.left is not None:
            self.left.inorder()
        print(self.data, end=" ")
        if self.right is not None:
            self.right.inorder()

    def postorder(self) -> None:
        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        print(self.data, end=" ")


if __name__ == "__main__":
    tree = BinaryTree(23)
    tree.insert(7)
    tree.insert(9)
    tree.insert(32)
    tree.insert(54)
    tree.insert(12)
    tree.insert(77)
    tree.insert(99)

    print(tree.search(54)) # True
    print(tree.height())

    tree.preorder() # 23 7 9 12 32 54 77 99
    print()
    tree.inorder() # 7 9 12 23 32 54 77 99
    print()
    tree.postorder() # 12 9 7 99 77 54 32 23
    print()
    print(tree.level_order_traversal()) # [[23], [7, 32], [9, 54], [12, 77], [99]]
    print(tree.level_order_with_queue()) # [23, 7, 32, 9, 54, 12, 77, 99]
