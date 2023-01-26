# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return [0, 0]
            leftsum = dfs(root.left)
            rightsum = dfs(root.right)

            withroot = root.val + leftsum[1] + rightsum[1]
            withoutroot = max(leftsum) + max(rightsum)
            return [withroot, withoutroot]

        return max(dfs(root))
