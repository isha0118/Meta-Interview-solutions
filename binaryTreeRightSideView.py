# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: Optional[TreeNode], level, ans):
        if root:
            if level==len(ans):
                ans.append(root.val)
            self.dfs(root.right, level+1, ans)
            self.dfs(root.left, level+1, ans)
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.dfs(root, 0, ans)
        return ans