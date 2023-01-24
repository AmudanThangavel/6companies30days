class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = None

    def add_node(self, data):
        new_node = TreeNode(data)

        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while current:
                if data < current.data:
                    if current.left is None:
                        current.left = new_node
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        break
                    else:
                        current = current.right


tree = Tree()

arr = [15, 3, 6, 77, 44, 34, 52, 21, 9]

for i in arr:
    tree.add_node(i)
