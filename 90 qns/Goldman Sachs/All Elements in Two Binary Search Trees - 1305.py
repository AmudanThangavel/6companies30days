# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def in_order(self, root):
        if root:
            self.in_order(root.left)
            self.values.append(root.val)
            self.in_order(root.right)

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        self.values = []
        self.in_order(root1)
        self.in_order(root2)
        return sorted(self.values)
