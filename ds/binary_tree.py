

class BinaryTree:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
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


    def preorder(self):
        print(self.data, end=" ")
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()

    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self.data, end=" ")
        if self.right is not None:
            self.right.inorder()

    def postorder(self):
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

    tree.preorder() # 23 7 9 12 32 54 77 99
    print()
    tree.inorder() # 7 9 12 23 32 54 77 99
    print()
    tree.postorder() # 12 9 7 99 77 54 32 23