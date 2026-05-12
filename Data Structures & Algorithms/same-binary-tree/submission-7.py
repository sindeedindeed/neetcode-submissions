# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None:
            return False
        
        while p.left is not None and q.left is not None:
            if (p.left.val != q.left.val):
                return False
            self.isSameTree(p.left, q.left)
        while p.right is not None and q.right is not None:
            if (p.right.val != q.right.val):
                return False
            self.isSameTree(p.right, q.right)
        return True

        
        