class Solution:
  def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if root is None or root == p or root == q:
        return root
    left_lca = self.lowestCommonAncestor(root.left, p, q)
    right_lca = self.lowestCommonAncestor(root.right, p, q)
    if left_lca is not None and right_lca is not None:
        return root
    return left_lca if left_lca is not None else right_lca