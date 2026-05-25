# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        curr = root
        left_depth = 0
        right_depth = 0
        while curr.left:
            curr = curr.left
            left_depth += 1
    
        curr = root
        while curr.right:
            curr = curr.right
            right_depth += 1
        
        return max(left_depth, right_depth)