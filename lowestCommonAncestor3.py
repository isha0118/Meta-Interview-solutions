"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p1, p2 = p, q
        while p1 != p2:
            p1 = p1.parent if p1 else q
            p2 = p2.parent if p2 else p
        return p1
# Initialization: Start two pointers, a and b, at nodes p and q, respectively.
# Traversal: Move each pointer to its parent node. If a pointer reaches the root (i.e., becomes None), redirect it to the other starting node.
# Convergence: The pointers will meet at the LCA of p and q
# The time complexity of this solution is O(h), where h is the height of the tree. In the worst case, both pointers will traverse the height of the tree twice (once to the root and once to the LCA).