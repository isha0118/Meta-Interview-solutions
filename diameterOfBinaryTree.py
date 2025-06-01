# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode], level=0) -> int:
        def longestPath(node):
            nonlocal diameter
            if not node:
                return 0
            left_path = longestPath(node.left)
            right_path = longestPath(node.right)
            diameter = max(diameter, left_path + right_path)
            return max(left_path, right_path) + 1
        diameter = 0    
        longestPath(root)
        return diameter